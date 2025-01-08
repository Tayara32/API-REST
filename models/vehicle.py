from sqlalchemy import ForeignKey

from utils.database import db


# Model definition for the 'Vehicle' table
def relationship(param, back_populates):
    pass


class Vehicle(db.Model):


    # Define columns for the table
    vehicle_id = db.Column(db.Integer, primary_key=True)
    brand =  db.Column(db.String(80), nullable=False)  # Added brand
    model =  db.Column(db.String(80), nullable=False)
    license_plate =  db.Column(db.String(20), unique=True, nullable=False)
    year =  db.Column(db.Integer, nullable=False)
    client_id =  db.Column(db.Integer, ForeignKey('clients.client_id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    relationship('Client', back_populates='vehicles')

    def __repr__(self):
        return (f"<Vehicle ID: {self.vehicle_id}, "
                f"Brand: {self.brand}, "
                f"Model: {self.model}, "
                f"License Plate: {self.license_plate}, "
                f"Year: {self.year}>")
