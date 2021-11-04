from main import ma 
from models.vehicles import Vehicle
from marshmallow_sqlalchemy import auto_field

class VehicleSchema(ma.SQLAlchemyAutoSchema):
    vehicle_id = auto_field(dump_only=True)
    
    class Meta:
        model = Vehicle
        load_instance = True
        
vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)