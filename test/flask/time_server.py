from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/time", methods=["GET"])
def time():
    """return current time"""
    return jsonify(datetime.now().strftime("%H:%M:%S"))


@app.route("/date", methods=["GET"])
def date():
    """return current date"""
    return jsonify(datetime.now().strftime("%Y-%m-%d"))


@app.route("/age", methods=["POST"])
def age():
    """incoming_json={"date":<"%m/%d/%Y">,"units":<year>}
    returns the length of time between the given date and the current time
    """
    incoming_json = request.get_json()
    date = incoming_json["date"]
    units = incoming_json["units"]
    if units == "years":
        return jsonify(
            (datetime.now() - datetime.strptime(date, "%m/%d/%Y")).days / 365
        )
    else:
        return jsonify("units not supported")


@app.route("/until_next_meal/<meal>", methods=["GET"])
def until_next_meal(meal):
    """Returns the number of hours until that meal"""
    if meal == "breakfast":
        return jsonify(
            (
                datetime.now().replace(hour=8, minute=0, second=0) - datetime.now()
            ).seconds
            / 3600
        )
    elif meal == "lunch":
        return jsonify(
            (
                datetime.now().replace(hour=12, minute=0, second=0) - datetime.now()
            ).seconds
            / 3600
        )
    elif meal == "dinner":
        return jsonify(
            (
                datetime.now().replace(hour=18, minute=0, second=0) - datetime.now()
            ).seconds
            / 3600
        )
    else:
        return jsonify("meal not supported")


if __name__ == "__main__":
    app.run()
