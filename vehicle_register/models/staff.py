from main import db

class Staff(db.Model):
        __tablename__ = "staff_members"
        staff_member_id = db.Column(db.Integer, primary_key=True)
        staff_member_name = db.Column(db.String(80), unique=True, nullable=False)
        
        def __init__(self, staff_member_name):
            self.staff_member_name = staff_member_name

        @property
        def serialize(self):
            return {
                "staff_id": self.staff_id,
                "staff_name": self.staff_name
            }