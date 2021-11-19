from main import db

class Vehicle(db.Model):
    
    __tablename__ = "vehicles"

    vehicle_id = db.Column(
        db.Integer, 
        primary_key=True)

    vehicle_rego = db.Column(
        db.String(80), 
        unique=True, 
        nullable=False)
    
    vehicle_make = db.Column(
        db.String(80), 
        unique=False, 
        nullable=True,
        default = "Speedracer")

    vehicle_checked_out = db.Column(
        db.Boolean(),
        nullable=True,
        default= False)

    @property
    def image_filename(self):
        return f"vehicle_images/{self.vehicle_id}.png"
    

    # def __init__(self, vehicle_rego, vehicle_make, vehicle_checked_out):
    #     self.vehicle_rego = vehicle_rego
    #     self.vehicle_make = vehicle_make
    #     self.vehicle_checked_out = vehicle_checked_out

    