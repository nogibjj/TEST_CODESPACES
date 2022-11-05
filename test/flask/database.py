from datetime import datetime
from flask import Flask, request, jsonify


db =[]

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_on():
    return jsonify("Server is on")

def add_patient(patient_name,pateint_id,blood_type,db):
    new_patirnt ={"name":patient_name,"id":pateint_id,"blood_type":blood_type}
    added_patient = new_patirnt.save()
    return added_patient


import data