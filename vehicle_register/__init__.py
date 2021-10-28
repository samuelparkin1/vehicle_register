from flask import Flask 

app = Flask (__name__)

@app.route('/', methods=["GET"])
def home_page():
    return "A table of vehicles"

@app.route('/staff',methods=["GET"])
def get_staff():
    return "A list of all registered staff members"

@app.route('/staff/sign_up',  methods=["POST"])
def post_staff_sign_up():
    return "Make a profile for a staff member"

@app.route('/staff/<int:id>/', methods=["GET"])
def get_staff_information(id):
    return f" staff information for user {id}"

@app.route("/vehicles/<int:id>/", methods=["DELETE"])
def staff_information_delete(id):
    return f" staff information for {id} has been deleted"

@app.route("/staff/<int:id>/", methods=["PUT", "PATCH"])
def staff_information_update(id):
    return f" staff information for user {id} has been updated"

@app.route('/vehicles', methods=["GET"])
def get_vehicles():
    return "A list of all registered vehicles"

@app.route('/vehicles/new_vehicle', methods=["POST"])
def post_new_vehicles():
    return "Make a profile for a new vehicle"

@app.route('/vehicles/<int:id>/', methods=["GET"])
def get_vehicle_information(id):
    return f" vehicle information for {id}\n""list of vehicle information"

@app.route("/vehicles/<int:id>/", methods=["PUT", "PATCH"])
def vehicles_information_update(id):
    return f" vehicle information for {id} has been updated"

@app.route("/vehicles/<int:id>/", methods=["DELETE"])
def vehicles_information_delete(id):
    return f" vehicle information for {id} has been deleted"

@app.route('/vehicles/<int:id>/photo',  methods=["POST"])
def post_vehicle_photos(id):
    return f" photos of {id}"

if __name__ == '__main__':
    app.run(debug=True)