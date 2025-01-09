from sqlalchemy import ForeignKey

from utils.database import db


# Model definition for the 'Work' table
def relationship(param, back_populates):
    pass


class Work(db.Model):


    # Define columns for the table
    work_id = db.Column(db.Integer, primary_key=True)
    cost =  db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    description =  db.Column(db.String(80), nullable=False)
    end_date = db.Column(db.Date)
    start_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(80))

    vehicle_id =  db.Column(db.Integer, ForeignKey('vehicle.vehicle_id'), nullable=False)
    relationship("Vehicle", back_populates="works")

    def __repr__(self):
        return (f"<Work ID: {self.work_id}, "
                f"Cost: {self.cost}, "
                f"Description: {self.description}, "
                f"Start Date: {self.start_date}, "
                f"End Date: {self.end_date}, "
                f"Status: {self.status}, "
                f"Vehicle ID: {self.vehicle_id}>")
