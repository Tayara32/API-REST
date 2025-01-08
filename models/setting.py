from sqlalchemy import ForeignKey

from utils.database import db


# Model definition for the 'Setting' table
def relationship(param, back_populates):
    pass


class Setting(db.Model):


    # Define columns for the table
    setting_id = db.Column(db.Integer, primary_key=True)
    key_name =  db.Column(db.String(80), nullable=False)
    updated_at =  db.Column(db.DateTime, server_default=db.func.now())
    value =  db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return (f"<Setting ID: {self.setting_id}, "
                f"Key Name: {self.key_name}, "
                f"Updated At: {self.updated_at}>, "
                f"Value: {self.value}")
