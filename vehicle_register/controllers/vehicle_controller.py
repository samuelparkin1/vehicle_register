from flask import Blueprint, jsonify, request
from main import db
from models.vehicles import Vehicle
from schemas.vehicle_schema import vehicle_schema, vehicles_schema

vehicles =Blueprint('vehicles', __name__)


# Vehicle CRUD

# This one is just a placeholder for now, no CRUD here
@vehicles.route('/')
def homepage():
    return "This is the home page"

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
        db.session.commit()
    return jsonify(vehicle_schema.dump(vehicle.first()))

@vehicles.route("/vehicles/<int:id>/", methods = ["DELETE"])
def delete_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify(vehicle_schema.dump(vehicle))

