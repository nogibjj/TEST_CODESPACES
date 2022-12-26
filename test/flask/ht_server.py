from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

db_patient = []
db_attend = []
logging.basicConfig(filename='server.log', level=logging.INFO)

# %% Echo's code


@app.route("/", methods=["GET"])
def server_status():
    """return server status"""
    return jsonify("Server is running")


@app.route("/api/new_attending", methods=["POST"])
def new_attending():
    """add a new attending to the attend database
    incoming json: {
"attending_username": <attending_username_string>,
"attending_email": <attending_email_string>,
"attending_phone": <attending_phone_string>
}
"""
    new_attending = request.get_json()
    db_attend.append(new_attending)
    return jsonify(db_attend), 200


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    """incoming json
{ "patient_id": <patient_id_string>,
"attending_username": <attending_username_string>,
    "patient_age": <patient_age_int>
}
"""
    """add a new patient to the db"""
    new_patient = request.get_json()
    patient_id = new_patient["patient_id"]
    try:
        patient_id = int(patient_id)
    except ValueError:
        return jsonify("Patient ID must be an integer"), 400
    patient_age = new_patient["patient_age"]
    try:
        patient_age = int(patient_age)
    except ValueError:
        return jsonify("Patient age must be an integer"), 400
    new_patient['heart_rate']= []
    new_patient['timestamp']= []
    db_patient.append(new_patient)
    return jsonify(db_patient), 200


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
    """return the status of a patient
    return dictionary: {
    "heart_rate": <heart_rate_integer>,
    "status":  <status_string>,
    "timestamp": <time_stamp_string>
}"""
    try:
        patient_id = int(patient_id)
    except ValueError:
        return jsonify("Patient ID must be an integer"), 400
    for patient in db_patient:
        if patient["patient_id"] == patient_id:
            return jsonify(patient), 200
    return jsonify("Patient ID not found"), 400


@app.route("/api/patients/<attedning_username>", methods=["GET"])
def patients(attedning_username):
    """return a list of all patients being seen by an attending"""
    return jsonify(db_patient), 200

# %% Rocio's code

# @app.route("/api/heart_rate", methods=["POST"])

# def heart_rate():
#     """incoming json
# { "patient_id": <patient_id_string>,
# "heart_rate": <heart_rate_int>
# }
# """
#     """add a new heart rate to the db"""
#     new_heart_rate = request.get_json()
#     db_patient.append(new_heart_rate)
#     return jsonify(db_patient), 200

# @app.route("/api/heart_rate/<patient_id>", methods=["GET"])
# def heart_rate(patient_id):
#     """return the heart rate of a patient"""
#     return jsonify(db_patient), 200

# @app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
# def heart_rate_average(patient_id):
#     """return the average heart rate of a patient"""
#     return jsonify(db_patient), 200

# @app.route("/api/heart_rate/interval_average", methods=["POST"])

# def heart_rate_interval_average():
#     """incoming json
# { "patient_id": <patient_id_string>,
# "heart_rate_average_since": <heart_rate_average_since_string>
# }
# """
#     """return the average heart rate of a patient over an interval"""
#     return jsonify(db_patient), 200
