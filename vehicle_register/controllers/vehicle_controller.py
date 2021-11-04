from flask import Blueprint, jsonify, request
from main import db
from models.vehicles import Vehicle
from models.staff import Staff

vehicles =Blueprint('vehicles', __name__)
staff =Blueprint('staff', __name__)

# Vehicle CRUD

# This one is just a placeholder for now, no CRUD here
@vehicles.route('/')
def homepage():
    """
    The homepage route. 
    
    This will later contain information about what classes are available to enroll in.
    '/' is the address here, which means it will be available from our host domain. 
    During production this is localhost:5000 or 127.0.0.1:5000
    """
    return "Hello, world! Check this out!"

@vehicles.route("/vehicles/", methods=["GET"])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([vehicle.serialize for vehicle in vehicles])

@vehicles.route("/vehicles/", methods=["POST"])
def create_vehicle():
    new_vehicle = Vehicle(request.json['vehicle_rego'])
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify(new_vehicle.serialize)

@vehicles.route("/vehicles/<int:id>/", methods = ["GET"])
def get_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    return jsonify(vehicle.serialize)

@vehicles.route("/vehicles/<int:id>/", methods=["PUT", "PATCH"])
def update_vehicle(id):
    vehicle = Vehicle.query.filter_by(vehicle_id=id)
    vehicle.update(dict(vehicle_rego = request.json["vehicle_rego"]))
    db.session.commit()
    return jsonify(vehicle.first().serialize)

@vehicles.route("/vehicles/<int:id>/", methods = ["DELETE"])
def delete_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify(vehicle.serialize)

# Staff CRUD

@staff.route("/staff_members/", methods=["GET"])
def get_staff_members():
    staff_members = Staff.query.all()
    return jsonify([staff.serialize for staff in staff_members])

@staff.route("/staff_members/", methods=["POST"])
def create_staff():
    new_staff = Staff(request.json['staff_name'])
    db.session.add(new_staff)
    db.session.commit()
    return jsonify(new_staff.serialize)

@staff.route("/staff_members/<int:id>/", methods = ["GET"])
def get_staff(id):
    staff = Staff.query.get_or_404(id)
    return jsonify(staff.serialize)

@staff.route("/staff_members/<int:id>/", methods=["PUT", "PATCH"])
def update_staff(id):
    staff = Staff.query.filter_by(staff_id=id)
    staff.update(dict(staff_name = request.json["staff_name"]))
    db.session.commit()
    return jsonify(staff.first().serialize)

@staff.route("/staff_members/<int:id>/", methods = ["DELETE"])
def delete_staff(id):
    staff = Staff.query.get_or_404(id)
    db.session.delete(staff)
    db.session.commit()
    return jsonify(staff.serialize)