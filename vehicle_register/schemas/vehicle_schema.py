from main import ma 
from models.vehicles import Vehicle
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length

class VehicleSchema(ma.SQLAlchemyAutoSchema):
    vehicle_id = auto_field(dump_only=True)
    vehicle_rego = auto_field(required=True, validate=Length(min=1))   
    vehicle_make = auto_field(required=True, validate=Length(min=1))
    vehicle_checked_out = auto_field(required=False, default= False)
    
    class Meta:
        model = Vehicle
        load_instance = True
        
vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)
vehicles_update_schema = VehicleSchema(partial=True)