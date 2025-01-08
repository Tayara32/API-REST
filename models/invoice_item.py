from sqlalchemy import ForeignKey

from utils.database import db


# Model definition for the 'Invoice_item' table
def relationship(param, back_populates):
    pass


class Invoice_item(db.Model):


    # Define columns for the table
    item_id = db.Column(db.Integer, primary_key=True)
    cost =  db.Column(db.Float)
    description =  db.Column(db.String(80), nullable=False)
    invoice_id =  db.Column(db.Integer, ForeignKey('invoice.invoice_id'), nullable=False)
    relationship("Invoice", back_populates="invoice_items")
    task_id =  db.Column(db.Integer, ForeignKey('task.task_id'), nullable=False)
    relationship("Task", back_populates="invoice_items")

    def __repr__(self):
        return (f"<Item ID: {self.item_id}, "
                f"Cost: {self.cost}, "
                f"Description: {self.description}, "
                f"Invoice ID: {self.invoice_id}, "
                f"Task ID: {self.task_id}>")
