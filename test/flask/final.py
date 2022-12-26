from flask import Flask,request ,jsonify
from pymodm import connect
# from database_definition import Patient


app = Flask(__name__)
db_patient = []

# server status and coonection to mongodb
@app.route("/", methods=["GET"])
def server_status():
    # test connection to mongodb 
    try:
        connect("mongodb://localhost:27017/healthcare")
        return "server running and connected to mongodb"
    except:
        return "server is down"
    # connect("mongodb+srv://echodpp:WiKMRhwb3symh7bL@bme547.kgv09vh.mongodb.net/final_db?retryWrites=true&w=majority")
    
    # return "Server is running"
    # return jsonify({"status": " server connected to database"})
        



# # get patient information
# @app.route("/new_patient", methods=["POST"])
# def new_patient():
#     upload = request.get_json()
#     # update information based on the primary key rec_no and save to database
    



if __name__ == "__main__":
    app.run()