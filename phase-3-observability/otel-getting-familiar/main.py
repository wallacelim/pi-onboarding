import concurrent.futures
import logging
from typing import TypedDict

from opentelemetry import metrics, trace
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.trace import Status, StatusCode
from opentelemetry.semconv.attributes.url_attributes import URL_FULL
from opentelemetry.semconv.attributes.http_attributes import HTTP_REQUEST_METHOD


class OrderItem(TypedDict):
    id: str


class Order(TypedDict):
    id: str
    amount: float
    items: list[OrderItem]
    email: str


OTLP_ENDPOINT = "http://localhost:4317"

# Traces
trace_provider = TracerProvider()
trace_provider.add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(endpoint=OTLP_ENDPOINT, insecure=True))
)
trace.set_tracer_provider(trace_provider)

# Metrics
metric_provider = MeterProvider(
    metric_readers=[
        PeriodicExportingMetricReader(
            OTLPMetricExporter(endpoint=OTLP_ENDPOINT, insecure=True)
        )
    ]
)
metrics.set_meter_provider(metric_provider)

# Logs
log_provider = LoggerProvider()
log_provider.add_log_record_processor(
    BatchLogRecordProcessor(OTLPLogExporter(endpoint=OTLP_ENDPOINT, insecure=True))
)
set_logger_provider(log_provider)
LoggingInstrumentor().instrument(set_logging_format=True)

logging.basicConfig(level=logging.INFO)
logging.getLogger("opentelemetry").setLevel(logging.DEBUG)
logger = logging.getLogger("orders.service")

tracer = trace.get_tracer("orders.service")
meter = metrics.get_meter("orders.metrics")

order_counter = meter.create_counter(
    "orders.created", description="Number of orders created"
)
payment_latency_ms = meter.create_histogram(
    "payment.latency", description="Payment processing time in milliseconds"
)


def process_order(order):
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order.id", order["id"])
        span.set_attribute("order.amount", order["amount"])
        span.add_event("order_received")
        logger.info("Processing order %s", order["id"], extra={"order.id": order["id"]})
        try:
            validate_order(order)
            reserve_inventory(order)
            charge_payment(order)
            send_confirmation_email(order)
            span.add_event("order_processed")
            order_counter.add(1, {"order.outcome": "success"})
            logger.info("Order %s completed", order["id"])

        except Exception as e:
            span.record_exception(e)
            span.set_status(Status(StatusCode.ERROR, str(e)))
            span.add_event("order_failed")
            order_counter.add(1, {"order.outcome": "error"})
            logger.error("Order %s failed: %s", order["id"], e)
            raise


@tracer.start_as_current_span("validate_order")
def validate_order(order):
    span = trace.get_current_span()
    span.set_attribute("order.items", len(order["items"]))

    if not order["items"]:
        raise ValueError("Order must contain at least one item")

    span.add_event("order_validated")


@tracer.start_as_current_span("reserve_inventory")
def reserve_inventory(order):
    for item in order["items"]:
        call_inventory_service(item)


@tracer.start_as_current_span("call_inventory_service")
def call_inventory_service(item):
    span = trace.get_current_span()
    span.set_attribute(HTTP_REQUEST_METHOD, "POST")
    span.set_attribute(URL_FULL, "https://inventory.internal/reserve")
    span.set_attribute("inventory.item_id", item["id"])
    span.add_event("inventory_reserved")


@tracer.start_as_current_span("charge_payment")
def charge_payment(order):
    span = trace.get_current_span()

    import time

    start = time.time()

    try:
        if order["amount"] > 1000:
            raise Exception("Payment declined")
    except Exception as e:
        span.record_exception(e)
        span.set_status(Status(StatusCode.ERROR))
        raise

    finally:
        payment_latency_ms.record(time.time() - start)


@tracer.start_as_current_span("send_order_confirmation_email")
def send_confirmation_email(order):
    span = trace.get_current_span()
    ctx = span.get_span_context()

    with tracer.start_as_current_span("email_worker", links=[trace.Link(ctx)]):
        span.add_event("confirmation_email_sent", {"email": order["email"]})


if __name__ == "__main__":
    orders: list[Order] = [
        {
            "id": "ord-001",
            "amount": 49.99,
            "items": [{"id": "item-a"}],
            "email": "alice@example.com",
        },
        {
            "id": "ord-002",
            "amount": 250.00,
            "items": [{"id": "item-b"}, {"id": "item-c"}],
            "email": "bob@example.com",
        },
        {
            "id": "ord-003",
            "amount": 1500.00,
            "items": [{"id": "item-d"}],
            "email": "carol@example.com",
        },  # will fail
        {
            "id": "ord-004",
            "amount": 0.00,
            "items": [],
            "email": "dave@example.com",
        },  # will fail (empty items)
        {
            "id": "ord-005",
            "amount": 999.99,
            "items": [{"id": "item-e"}, {"id": "item-f"}, {"id": "item-g"}],
            "email": "eve@example.com",
        },
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(process_order, order): order["id"] for order in orders
        }
        for future in concurrent.futures.as_completed(futures):
            order_id = futures[future]
            try:
                future.result()
                print(f"[{order_id}] completed successfully")
            except Exception as e:
                print(f"[{order_id}] failed: {e}")

    trace_provider.shutdown()
    metric_provider.shutdown()
    log_provider.shutdown()
