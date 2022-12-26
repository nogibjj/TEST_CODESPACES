from datetime import datetime


def get_average(in_data, db_patient):
    """return the average heart rate of a patient  after a given time
    :param in_data: JSON contains keys "patient_id" and
    "heart_rate_average_since".
    :return: integer of average heart rate"""

    if type(in_data) is not dict:
        return ("input json should be a dictionary", 400)
    try:
        patient_id = int(in_data["patient_id"])
    except ValueError:
        return ("Patient ID must can be convert to an integer", 400)
    try:
        time_since = datetime.strptime(in_data["heart_rate_average_since"],
                                       "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return ("Time must be in format YYYY-MM-DD HH:MM:SS", 400)
    p_found = None
    for patient in db_patient:
        if patient["patient_id"] == patient_id:
            p_found = patient
            break
    if p_found is None:
        return ("Patient ID not found", 400)
    heart_rate = p_found["heart_rate"]
    timestamp = p_found["timestamp"]
    if len(heart_rate) != len(timestamp):
        return ("Patient has different amount of heart rate and timestamp", 400)
    timestamp = [datetime.strptime(t, "%Y-%m-%d %H:%M:%S") for t in timestamp]
    average = 0
    count = 0
    for i in range(len(timestamp)):
        if timestamp[i] > time_since:
            average += heart_rate[i]
            count += 1
    if count == 0:
        return ("No heart rate recorded after given time", 400)
    return (int(average/count), 200)

# def find_patient(patient_id, db_patient=db_patient):
#     """return patient info
#     :param patient_id: patient id integer
#     :return: patient info dictionary"""

#     for patient in db_patient:
#         if patient["patient_id"] == patient_id:
#             return patient
#     return "Patient ID not found"
