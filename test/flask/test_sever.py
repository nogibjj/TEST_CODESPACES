from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"

@app.route("/new_patient", methods=["POST"])
def new_patient():
    json_data = request.get_json()
    expected =[type(json_data['rec_no']), type(json_data['patient_name']), type(json_data['hr']), type(json_data['ECG_trace']), type(json_data['med_im'])]
    print(json_data['rec_no'])
    print(json_data)
    return "{}".format(expected)


if __name__ == "__main__":
    app.run()