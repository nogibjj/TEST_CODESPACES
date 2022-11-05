# from flask import Flask, request, jsonify

# app = Flask(__name__)

# db = []


# @app.route("/", methods=["GET"])
# def server_status():
#     """return server status"""
#     return jsonify("Server is running")


# def add_test(id, test_name, test_result):
#     """adds a test to the database"""
#     new_test = {
#         "id": id,
#         "test_name": test_name,
#         "test_result": test_result,
#     }
#     db.append(new_test)


# def init_server():
#     add_test(1, "hdl", 33)
#     add_test(2, "ldl", 44)


# @app.route("/new_test", methods=["POST"])
# def add_new_test():
#     """
#     recieve data from post request
#     call other functions to do all the work
#     return information
#     """
#     in_data = request.get_json()
#     message, status_code = add_new_test_worker(in_data)
#     return jsonify(message), status_code


# def add_new_test_worker(in_data):
#     validation_result = validate_new_test(in_data)
#     if validation_result is not True:
#         return result, 400
#     add_test(in_data["id"], in_data["test_name"], in_data["test_result"])
#     return "test added", 200


# def validate_new_test(in_data):
#     if type(in_data) is not dict:
#         return "post data was not a dictionary"
#     excepted_keys = ["id", "test_name", "test_result"]
#     for key in excepted_keys:
#         if key not in in_data:
#             return "missing key: " + key
#     expected_types = {"id": int, "test_name": str, "test_result": int}
#     for key in excepted_keys:
#         if type(in_data[key]) is not expected_types[key]:
#             return "wrong type for " + key
#     return True


# if __name__ == "__main__":
#     init_server()
#     app.run(port=5000)
#     print(db)


# @app.route("/add_test", methods=["POST"])
# def add_test_flask_handler():
#     """
#     recieve data from post request
#     call other functions to do all the work
#     return information
#     """
#     in_data = request.get_json()
#     message, status_code = add_test_worker(in_data)
#     return jsonify(message), status_code


# def add_test_worker(in_data):
#     validation_result = add_test_validation(in_data)
#     if validation_result is not True:
#         return result, 400
#     add_test_to_patient(in_data)
#     return "test added", 200


# def add_test_to_patient(in_data):
#     patient = find_patient(in_data["id"])
#     patient["test_name"].append(in_data["test_name"])
#     patient["test_result"].append(in_data["test_result"])
#     print_database()


# def add_test_validation(in_data):
#     if type(in_data) is not dict:
#         return "post data was not a dictionary"
#     excepted_keys = ["id", "test_name", "test_result"]
#     for key in excepted_keys:
#         if key not in in_data:
#             return "missing key: " + key
#     expected_types = {"id": int, "test_name": str, "test_result": int}
#     for key in excepted_keys:
#         if type(in_data[key]) is not expected_types[key]:
#             return "wrong type for " + key
#     return True


# def find_patient(id):
#     for patient in db:
#         if patient["id"] == id:
#             return patient
#     return None


# def print_database():
#     for patient in db:
#         print(patient)


# if __name__ == "__main__":
#     init_server()
#     app.run(port=5000)


# logging.basicConfig(filename='test.log', level=logging.DEBUG)

from flask import Flask, request, jsonify

app = Flask(__name__)

db = []


@app.route("/", methods=["GET"])
def server_status():
    """return server status"""
    return jsonify("Server is running")


def init_database():
    """initialize database"""
    global db
    db = [
        {
            "patient_id": 1,
            "attending_username": "John Doe",
            "age": 25,
            "patient_age": "123 Main Street",
            "heart_rate": "555-555-5555",
        },
        {
            "patient_id": 2,
            "attending_username": "Jane Doe",
            "age": 30,
            "patient_age": "456 Main Street",
            "heart_rate": "555-555-5555",
        },
    ]
