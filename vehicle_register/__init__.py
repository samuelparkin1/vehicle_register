from flask import Flask 

app = Flask (__name__)

@app.route('/')
def home_page():
    return "A table of vehicles"

@app.route('/staff')
def get_staff():
    return "A list of all registered staff members"

@app.route('/staff/sign_up')
def post_staff_sign_up():
    return "Make a profile for a staff member"

@app.route('/staff/<int:id>/')
def get_staff_information(id):
    return f" staff information for user {id}\n""list of staff members information"

@app.route('/vehicles')
def get_vehicles():
    return "A list of all registered vehicles"

@app.route('/vehicles/new_vehicle')
def post_new_vehicles():
    return "Make a profile for a new vehicle"

@app.route('/vehicles/<int:id>/')
def get_vehicle_information(id):
    return f" vehicle information for {id}\n""list of vehicle information"

@app.route('/vehicles/<int:id>/photo')
def post_vehicle_photos(id):
    return f" photos of {id}"

if __name__ == '__main__':
    app.run(debug=True)