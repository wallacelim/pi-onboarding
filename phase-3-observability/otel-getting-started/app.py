from random import randint
from flask import Flask, request
import logging
from opentelemetry import trace, metrics


tracer = trace.get_tracer("diceroller.tracer")
meter = metrics.get_meter("diceroller.meter")

roll_counter = meter.create_counter(
    "dice.rolls", description="Number of rolls by roll value"
)
roll_histo = meter.create_histogram(
    "dice.rolls", description="Histogram of rolls by roll value"
)

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/rolldice")
def roll_dice():
    with tracer.start_as_current_span("roll") as roll_span:
        player = request.args.get("player", default=None, type=str)
        result = str(roll())
        roll_span.set_attribute("roll.value", result)
        roll_counter.add(1, {"roll.value": result})
        roll_histo.record(int(result), {"roll.value": result})
        roll_span.add_event(
            "Dice rolled", {"player": player or "unknown player", "result": result}
        )
        if player:
            logger.warning("%s is rolling the dice: %s", player, result)
        else:
            logger.warning("Anonymous player is rolling the dice: %s", result)
        return result


def roll():
    return randint(1, 6)
