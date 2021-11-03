import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

def create_app ():

    # Creates a Flask App
    app = Flask (__name__)

    app.config.from_object("config.app_config")

    # Allows python to communicate to database 
    db= SQLAlchemy(app)



    class Vehicle(db.Model):
        # Does this create the table 'vehicle' if it does't exist????
        __tablename__ = "vehicles"

        # Does this make a serial key???
        vehicle_id = db.Column(db.Integer, primary_key=True)
        vehicle_rego = db.Column(db.String(80), unique=True, nullable=False)
        
        def __init__(self, vehicle_rego):
            self.vehicle_rego = vehicle_rego

        @property
        def serialize(self):
            return {
                "vehicle_id": self.vehicle_id,
                "vehicle_rego": self.vehicle_rego
            }
    class Staff(db.Model):
        __tablename__ = "staff_members"
        staff_id = db.Column(db.Integer, primary_key=True)
        staff_name = db.Column(db.String(80), unique=True, nullable=False)
        
        def __init__(self, staff_name):
            self.staff_name = staff_name

        @property
        def serialize(self):
            return {
                "staff_id": self.staff_id,
                "staff_name": self.staff_name
            }

    # Not sure what this does?????
    # Is db from SQLAlchemy????
    db.create_all()

    # Vehicle CRUD

    @app.route("/vehicles/", methods=["GET"])
    def get_vehicles():
        vehicles = Vehicle.query.all()
        return jsonify([vehicle.serialize for vehicle in vehicles])

    @app.route("/vehicles/", methods=["POST"])
    def create_vehicle():
        new_vehicle = Vehicle(request.json['vehicle_rego'])
        db.session.add(new_vehicle)
        db.session.commit()
        return jsonify(new_vehicle.serialize)
    
    @app.route("/vehicles/<int:id>/", methods = ["GET"])
    def get_vehicle(id):
        vehicle = Vehicle.query.get_or_404(id)
        return jsonify(vehicle.serialize)

    @app.route("/vehicles/<int:id>/", methods=["PUT", "PATCH"])
    def update_vehicle(id):
        vehicle = Vehicle.query.filter_by(vehicle_id=id)
        vehicle.update(dict(vehicle_rego = request.json["vehicle_rego"]))
        db.session.commit()
        return jsonify(vehicle.first().serialize)

    @app.route("/vehicles/<int:id>/", methods = ["DELETE"])
    def delete_vehicle(id):
        vehicle = Vehicle.query.get_or_404(id)
        db.session.delete(vehicle)
        db.session.commit()
        return jsonify(vehicle.serialize)

    # Staff CRUD

    @app.route("/staff_members/", methods=["GET"])
    def get_staff_members():
        staff_members = Staff.query.all()
        return jsonify([staff.serialize for staff in staff_members])

    @app.route("/staff_members/", methods=["POST"])
    def create_staff():
        new_staff = Staff(request.json['staff_name'])
        db.session.add(new_staff)
        db.session.commit()
        return jsonify(new_staff.serialize)

    @app.route("/staff_members/<int:id>/", methods = ["GET"])
    def get_staff(id):
        staff = Staff.query.get_or_404(id)
        return jsonify(staff.serialize)

    @app.route("/staff_members/<int:id>/", methods=["PUT", "PATCH"])
    def update_staff(id):
        staff = Staff.query.filter_by(staff_id=id)
        staff.update(dict(staff_name = request.json["staff_name"]))
        db.session.commit()
        return jsonify(staff.first().serialize)

    @app.route("/staff_members/<int:id>/", methods = ["DELETE"])
    def delete_staff(id):
        staff = Staff.query.get_or_404(id)
        db.session.delete(staff)
        db.session.commit()
        return jsonify(staff.serialize)

    return app