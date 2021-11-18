from flask import Blueprint, jsonify, request, render_template, redirect, url_for, abort
from main import db
from models.vehicles import Vehicle
from schemas.vehicle_schema import vehicles_schema, vehicle_schema
from flask_login import login_required, current_user

vehicles = Blueprint('vehicles', __name__)

# This one is just a placeholder for now, no CRUD here
@vehicles.route('/')
def homepage():
    data = {
        "page_title": "Homepage"
    }
    return render_template("homepage.html", page_data=data)

# The GET routes endpoint
@vehicles.route("/vehicles/", methods=["GET"])
def get_vehicles():
    data = {
        "page_title": "Vehicle Index",
        "vehicles": vehicles_schema.dump(Vehicle.query.all())
    }
    return render_template("vehicle_index.html", page_data=data)

# The POST route endpoint
@vehicles.route("/vehicles/", methods=["POST"])
def create_vehicle():
    new_vehicle=vehicle_schema.load(request.form)
    db.session.add(new_vehicle)
    db.session.commit()
    return redirect(url_for("vehicles.get_vehicles"))

# An endpoint to GET info about a specific vehicle
@vehicles.route("/vehicles/<int:id>/", methods = ["GET"])
def get_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    data = {
        "page_title": "Vehicle Detail",
        "vehicle": vehicle_schema.dump(vehicle)
    }
    return render_template("vehicle_detail.html", page_data=data)

# A PUT/PATCH route to update vehicle info
@vehicles.route("/vehicles/<int:id>/", methods=["POST"])
def update_vehicle(id):
    vehicle = Vehicle.query.filter_by(vehicle_id=id)
   
    updated_fields = vehicle_schema.dump(request.form)
    if updated_fields:
        vehicle.update(updated_fields)
        db.session.commit()

    data = {
        "page_title": "Vehicle Detail",
        "vehicle": vehicle_schema.dump(vehicle.first())
    }
    return render_template("vehicle_detail.html", page_data=data)

# Finally, we round out our CRUD resource with a DELETE method
@vehicles.route("/vehicles/<int:id>/delete/", methods=["POST"])
def delete_vehicle(id):
    # Can't delete a vehicle that doesn't exist, so get_or_404 here is correct
    vehicle = Vehicle.query.get_or_404(id)
    # delete the vehicle and commit the transaction
    db.session.delete(vehicle)
    db.session.commit()
    # We deleted the row in the database but we still have the python object
    # since we fetched it before we called session.delete, so we can 
    # serialize it and return it to the user to show them what they deleted!
    return redirect(url_for("vehicles.get_vehicles"))