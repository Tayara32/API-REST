import logging
from models.invoice_item import Invoice_item
from utils.database import db

logger = logging.getLogger(__name__)

def get_all_invoice_items():
    """
    Retrieve all invoice_items.
    :return: list: A list of dictionaries containing information about all invoice_items.
    """
    try:
        invoice_items = Invoice_item.query.all()
        return [
            {
                "item_id": invoice_item.item_id,
                "cost": invoice_item.cost,
                "description": invoice_item.description,
                "invoice_id": invoice_item.invoice_id,
                "task_id": invoice_item.task_id,
            }
            for invoice_item in invoice_items
        ]
    except Exception as e:
        logger.error(f"Error fetching all invoice_items: {e}")
        return {"error": "Internal Server Error"}

def get_invoice_item(item_id):
    """
    Retrieve an invoice_item by ID.
    :param item_id: The ID of the invoice_item to retrieve.
    :return: dict: A dictionary containing the invoice_item's information or an error message.
    """
    try:
        invoice_item = Invoice_item.query.get(item_id)
        if not invoice_item:
            return None
        return {
            "item_id": invoice_item.item_id,
            "cost": invoice_item.cost,
            "description": invoice_item.description,
            "invoice_id": invoice_item.invoice_id,
            "task_id": invoice_item.task_id,
        }
    except Exception as e:
        logger.error(f"Error fetching invoice_item {item_id}: {e}")
        return {"error": "Internal Server Error"}

def create_invoice_item(cost, description, invoice_id, task_id):
    """
    Create a new invoice_item entry.
    :param cost: The cost of the invoice_item.
    :param description: Description of the invoice_item.
    :param invoice_id: The ID of the associated invoice
    :param task_id: The ID of the associated task.
    :return: dict: A dictionary containing the newly created invoice_item's information or an error message.
    """
    try:
        invoice_item = Invoice_item(
            cost=cost,
            description=description,
            invoice_id=invoice_id,
            task_id=task_id,
        )
        db.session.add(invoice_item)
        db.session.commit()
        return {
            "item_id": invoice_item.item_id,
            "cost": invoice_item.cost,
            "description": invoice_item.description,
            "invoice_id": invoice_item.invoice_id,
            "task_id": invoice_item.task_id,
        }
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating invoice_item: {e}")
        return {"error": "Internal Server Error"}

def update_invoice_item(item_id, cost=None, description=None, invoice_id=None, task_id=None):
    """
    Update an existing invoice_item.
    :param item_id: The ID of the invoice_item to update.
    :param cost: The updated cost.
    :param description: The updated description.
    :param invoice_id: The updated invoice ID.
    :param task_id: The updated task ID.
    :return: dict: A dictionary containing the updated invoice_item's information or an error message.
    """
    try:
        invoice_item = Invoice_item.query.get(item_id)
        if not invoice_item:
            return None

        invoice_item.cost = cost if cost is not None else invoice_item.cost
        invoice_item.description = description if description else invoice_item.description
        invoice_item.invoice_id = invoice_id if invoice_id else invoice_item.invoice_id
        invoice_item.task_id = task_id if task_id else invoice_item.task_id

        db.session.commit()
        return {
            "item_id": invoice_item.item_id,
            "cost": invoice_item.cost,
            "description": invoice_item.description,
            "invoice_id": invoice_item.invoice_id,
            "task_id": invoice_item.task_id,
        }
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating invoice_item {item_id}: {e}")
        return {"error": "Internal Server Error"}

def delete_invoice_item(item_id):
    """
    Delete an invoice_item entry.
    :param item_id: The ID of the invoice_item to delete.
    :return: dict: A message confirming deletion or an error message.
    """
    try:
        invoice_item = Invoice_item.query.get(item_id)
        if not invoice_item:
            return None
        db.session.delete(invoice_item)
        db.session.commit()
        return {"message": f"invoice_item {item_id} deleted successfully"}
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error deleting invoice_item {item_id}: {e}")
        return {"error": "Internal Server Error"}
