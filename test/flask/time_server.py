from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def server_status():
    return "Server is running"


@app.route("/time", methods=["GET"])
def time():
    """return current time"""
    current_time = datetime.now().strftime("%H:%M:%S")
    return jsonify(str(current_time))


@app.route("/date", methods=["GET"])
def date():
    """return current date"""
    current_date = datetime.now().strftime("%Y-%m-%d")
    return jsonify(str(current_date))


@app.route("/age", methods=["POST"])
def age():
    """incoming_json={"date":<"%m/%d/%Y">,"units":<year>}
    returns the length of time between the given date and 
    the current time
    """
    incoming_json = request.get_json()
    date = incoming_json["date"]
    units = incoming_json["units"]
    if units == "years":
        age = datetime.now().year - datetime.strptime(date, "%m/%d/%Y").year
        return jsonify(float(age))
    else:
        return jsonify("units not supported")


@app.route("/until_next_meal/<meal>", methods=["GET"])
def until_next_meal(meal):
    """Returns the number of hours until that meal"""
    if meal == "breakfast":
        breakfast = (
            datetime.now().replace
            (hour=8, minute=0, second=0) - datetime.now()
        ).seconds / 3600
        return jsonify((float(round(breakfast, 1))))
    elif meal == "lunch":
        lunch = (
            datetime.now().replace
            (hour=12, minute=0, second=0) - datetime.now()
        ).seconds / 3600
        return jsonify((float(round(lunch, 1))))
    elif meal == "dinner":
        dinner = (
            datetime.now().replace
            (hour=18, minute=0, second=0) - datetime.now()
        ).seconds / 3600
        return jsonify((float(round(dinner, 1))))
    else:
        return jsonify("meal not supported")


if __name__ == "__main__":
    app.run()
