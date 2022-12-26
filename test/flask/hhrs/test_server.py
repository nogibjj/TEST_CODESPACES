from datetime import datetime

def test_get_average():
    from server import get_average
    """test the get_average function"""
    patient1= {"patient_id": 1, "heart_rate": [108, 120, 130, 140, 150],"timestamp": ["2018-03-09 11:00:36", "2018-03-09 11:01:36", "2018-03-09 11:02:36", "2018-03-09 11:03:36", "2018-03-09 11:04:36"]}
    patient2= {"patient_id": 2, "heart_rate": [100, 120, 130, 140, 150],"timestamp": ["2018-03-09 11:00:36", "2018-03-09 11:01:36", "2018-03-09 11:02:36", "2018-03-09 11:03:36", "2018-03-09 11:04:36"]}
    db_patient = [patient1, patient2]
    in_data = {"patient_id": 1, "heart_rate_average_since": "2018-03-09 11:02:36"}
    print(get_average(in_data, db_patient))
    in_data2 = {"patient_id": 2, "heart_rate_average_since": "2018-03-09 11:05:36"}
    print(get_average(in_data2, db_patient))
    in_data3 = {"patient_id": 4, "heart_rate_average_since": "2018-03-09 11:00:36"}
    print(get_average(in_data3, db_patient))


if __name__ == "__main__":
    test_get_average()