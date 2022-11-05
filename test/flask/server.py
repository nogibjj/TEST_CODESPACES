from crypt import methods
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route(
    "/", methods=["GET"]
)  # this decorator tell us which URL should trigger our function
def server_status():
    return "Server is running"


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"


# can not check browser with post request
@app.route("/hdl_check", methods=["POST"])
def hdl_check_from_internet():
    """
    incoming_json={"name":<name_str>
                    "hdl_value":<hdl_value_int>
                    }
    """
    from bloodcalculator import check_HDL

    incoming_json = request.get_json()
    hdl_value = incoming_json["hdl_value"]
    name = incoming_json["name"]
    # print to terminal can used for debug
    print("the received valiu is", hdl_value)
    hdl_analysis = check_HDL(hdl_value)
    return hdl_analysis  # client will only recieve what is returned


@app.route("/add", methods=["POST"])
def add():
    """add two numbers"""
    incoming_json = request.get_json()
    a = incoming_json["a"]
    b = incoming_json["b"]
    # jsonify is used to convert python object to json object best choice for return
    return jsonify(a+b)


if __name__ == "__main__":
    app.run()  # default port is 5000 host="0.0.0.0" # to make it visible to other devices in the network
