import logging
from models.invoice import Invoice
from utils.database import db

logger = logging.getLogger(__name__)

def get_all_invoices():
    """
    Retrieve all works.
    :return: list: A list of dictionaries containing information about all works.
    """
    try:
        invoices = Invoice.query.all()
        return [
            {
                "invoice_id": invoice.invoice_id,
                "issued_at": invoice.issued_at,
                "iva": invoice.iva,
                "total": invoice.total,
                "total_with_iva": invoice.total_with_iva,
                "client_id": invoice.client_id,
            }
            for invoice in invoices
        ]
    except Exception as e:
        logger.error(f"Error fetching all invoices: {e}")
        return {"error": "Internal Server Error"}

def get_invoice(invoice_id):
    """
    Retrieve an invoice by ID.
    :param invoice_id: The ID of the invoice to retrieve.
    :return: dict: A dictionary containing the invoice's information or an error message.
    """
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return None
        return {
            "invoice_id": invoice.invoice_id,
            "issued_at": invoice.issued_at,
            "iva": invoice.iva,
            "total": invoice.total,
            "total_with_iva": invoice.total_with_iva,
            "client_id": invoice.client_id,
        }
    except Exception as e:
        logger.error(f"Error fetching invoice {invoice_id}: {e}")
        return {"error": "Internal Server Error"}

def create_invoice(issued_at, iva, total, total_with_iva, client_id):
    """
    Create a new invoice entry.
    :param issued_at: The datetime the invoice was issued.
    :param iva: Iva applied on the invoice.
    :param total: Total value (without iva) of the invoice.
    :param total_with_iva: Total value (with iva) of the invoice.
    :param client_id: The ID of the associated client.
    :return: dict: A dictionary containing the newly created invoice's information or an error message.
    """
    try:
        invoice = Invoice(
            issued_at=issued_at,
            iva=iva,
            total=total,
            total_with_iva=total_with_iva,
            client_id=client_id,
        )
        db.session.add(invoice)
        db.session.commit()
        return {
            "invoice_id": invoice.invoice_id,
            "issued_at": invoice.issued_at,
            "iva": invoice.iva,
            "total": invoice.total,
            "total_with_iva": invoice.total_with_iva,
            "client_id": invoice.client_id,
        }
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating invoice: {e}")
        return {"error": "Internal Server Error"}

def update_invoice(invoice_id, issued_at, iva=None, total=None, total_with_iva=None, client_id=None):
    """
    Update an existing invoice.
    :param invoice_id: The ID of the invoice to update.
    :param issued_at: The updated datetime the invoice was issued_at.
    :param iva: Updated iva applied on the invoice.
    :param total: Updated total value (without iva) of the invoice.
    :param total_with_iva: Updated total value (with iva) of the invoice.
    :param client_id: Updated ID of the associated client.
    :return: dict: A dictionary containing the updated invoice's information or an error message.
    """
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return None

        invoice.issued_at = issued_at if issued_at is not None else invoice.issued_at
        invoice.iva = iva if iva is not None else invoice.iva
        invoice.total = total if total is not None else invoice.total
        invoice.total_with_iva = total_with_iva if total_with_iva is not None else invoice.total_with_iva
        invoice.client_id = client_id if client_id is not None else invoice.vehicle_id

        db.session.commit()
        return {
            "invoice_id": invoice.invoice_id,
            "issued_at": invoice.issued_at,
            "iva": invoice.iva,
            "total": invoice.total,
            "total_with_iva": invoice.total_with_iva,
            "client_id": invoice.client_id,
        }
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating invoice {invoice_id}: {e}")
        return {"error": "Internal Server Error"}

def delete_invoice(invoice_id):
    """
    Delete an invoice entry.
    :param invoice_id: The ID of the invoice to delete.
    :return: dict: A message confirming deletion or an error message.
    """
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return None
        db.session.delete(invoice)
        db.session.commit()
        return {"message": f"Invoice {invoice_id} deleted successfully"}
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error deleting invoice {invoice_id}: {e}")
        return {"error": "Internal Server Error"}
