from sqlalchemy import ForeignKey
from utils.database import db


# Modelo Invoice
def relationship(param, back_populates):
    pass


class Invoice(db.Model):

    # Define colunas para a tabela
    invoice_id = db.Column(db.Integer, primary_key=True)
    issued_at = db.Column(db.DateTime, server_default=db.func.now())
    iva = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    total_with_iva = db.Column(db.Float, nullable=False)

    client_id = db.Column(db.Integer, ForeignKey('client.client_id'), nullable=False)
    relationship("Client", back_populates="invoices")

    def __repr__(self):
        return (f"<Invoice ID: {self.invoice_id}, "
                f"Issued At: {self.issued_at}, "
                f"Iva: {self.iva}, "
                f"Total: {self.total}, "
                f"Total With Iva: {self.total_with_iva}, "
                f"Client ID: {self.client_id}")
