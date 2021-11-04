from flask import Blueprint, jsonify, request
from main import db
from models.staff import Staff
from schemas.staff_schema import staff_member_schema, staff_members_schema

staff = Blueprint('staff', __name__)

# Staff CRUD

@staff.route("/staff_members/", methods=["GET"])
def get_staff_members():
    staff_members = Staff.query.all()
    return jsonify(staff_members_schema.dump(staff_members))

@staff.route("/staff_members/", methods=["POST"])
def create_staff():
    new_staff = staff_member_schema.load (request.json)
    db.session.add(new_staff)
    db.session.commit()
    return jsonify(staff_member_schema.dump(new_staff))

@staff.route("/staff_members/<int:id>/", methods = ["GET"])
def get_staff(id):
    staff_member = Staff.query.get_or_404(id)
    return jsonify(staff_member_schema.dump(staff_member))

@staff.route("/staff_members/<int:id>/", methods=["PUT", "PATCH"])
def update_staff(id):
    staff_member = Staff.query.filter_by(staff_member_id=id)
    updated_fields = staff_member_schema.dump(request.json)
    if updated_fields:
        staff_member.update(updated_fields)
        db.session.commit()
    return jsonify(staff_member_schema.dump(staff_member.first()))

@staff.route("/staff_members/<int:id>/", methods = ["DELETE"])
def delete_staff(id):
    staff = Staff.query.get_or_404(id)
    db.session.delete(staff)
    db.session.commit()
    return jsonify(staff.serialize)