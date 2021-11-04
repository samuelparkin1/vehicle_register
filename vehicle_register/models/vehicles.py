
from main import db

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
    