from flask import Blueprint, jsonify, request
from main import db
from models.vehicles import Vehicle
from models.staff import Staff
from schemas.vehicle_schema import vehicle_schema, vehicles_schema

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
    return jsonify(vehicles_schema.dump(vehicles))

@vehicles.route("/vehicles/", methods=["POST"])
def create_vehicle():
    new_vehicle = vehicle_schema.load (request.json)
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify(vehicle_schema.dump(new_vehicle))

@vehicles.route("/vehicles/<int:id>/", methods = ["GET"])
def get_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    return jsonify (vehicle_schema.dump(vehicle))

@vehicles.route("/vehicles/<int:id>/", methods=["PUT", "PATCH"])
def update_vehicle(id):
    vehicle = Vehicle.query.filter_by(vehicle_id=id)
    updated_fields = vehicle_schema.dump(request.json)
    if updated_fields:
        vehicle.update(updated_fields)
        db.sessions.commit()
    vehicle.update()
    db.session.commit()
    return jsonify(vehicle_schema.dump(Vehicle.first()))

@vehicles.route("/vehicles/<int:id>/", methods = ["DELETE"])
def delete_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify(vehicle_schema.dump(vehicle))

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