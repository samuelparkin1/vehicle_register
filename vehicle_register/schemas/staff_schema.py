from main import ma 
from models.staff import Staff
from marshmallow_sqlalchemy import auto_field

class StaffSchema(ma.SQLAlchemyAutoSchema):
    staff_member_id = auto_field(dump_only=True)
    
    class Meta:
        model = Staff
        load_instance = True
        
staff_member_schema = StaffSchema()
staff_members_schema = StaffSchema(many=True)