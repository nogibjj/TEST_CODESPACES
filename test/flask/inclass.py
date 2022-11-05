from unicodedata import name
from flask import Flask, request, jsonify

app = Flask(__name__)

db = []


@app.route("/", methods=["GET"])
def server_status():
    """return server status"""
    return jsonify("Server is running")


def add_patient(patient_name, patient_id, blood_type):
    """adds a patient to the database"""
    new_patient = {
        "name": patient_name,
        "id": patient_id,
        "blood_type": blood_type,
        "test_name": [],
        "test_result": [],
    }
    db.append(new_patient)


def init_server():
    add_patient("John", 1, "A")
    add_patient("Mary", 2, "B")


if __name__ == "__main__":
    init_server()
    app.run(debug=True, port=5000)


@app.route("/new_patient", methods=["POST"])
def add_new_patient():
    """
    recieve data from post request
    call other functions to do all the work
    return information
    """
    in_data = request.get_json()
    message, status_code = add_new_patient_worker(in_data)
    return jsonify(message), status_code


def add_new_patient_worker(in_data):
    validation_result = validate_new_patient(in_data)
    if validation_result is not True:
        return result, 400
    add_patient(in_data["name"], in_data["id"], in_data["blood_type"])
    return "patient added", 200


def validate_new_patient(in_data):
    if type(in_data) is not dict:
        return "post data was not a dictionary"
    excepted_keys = ["name", "id", "blood_type"]
    for key in excepted_keys:
        if key not in in_data:
            return "missing key: " + key
    expected_types = [str, int, str]
    for key, expected_type in zip(excepted_keys, expected_types):
        if type(in_data[key]) is not expected_type:
            return "key " + key + " was not of type " + str(expected_type)
    return True


if __name__ == "__main__":
    init_server()
    app.run(debug=True, port=5000)
