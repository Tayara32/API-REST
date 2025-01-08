import logging
from models.work import Work
from utils.database import db

logger = logging.getLogger(__name__)

def get_all_work():
    """
    Retrieve all works.
    :return: list: A list of dictionaries containing information about all works.
    """
    try:
        works = Work.query.all()
        return [
            {
                "work_id": work.work_id,
                "cost": work.cost,
                "description": work.description,
                "start_date": work.start_date,
                "end_date": work.end_date,
                "status": work.status,
                "vehicle_id": work.vehicle_id,
                "created_at": work.created_at,
            }
            for work in works
        ]
    except Exception as e:
        logger.error(f"Error fetching all works: {e}")
        return {"error": "Internal Server Error"}

def get_work(work_id):
    """
    Retrieve a work by ID.
    :param work_id: The ID of the work to retrieve.
    :return: dict: A dictionary containing the work's information or an error message.
    """
    try:
        work = Work.query.get(work_id)
        if not work:
            return None
        return {
            "work_id": work.work_id,
            "cost": work.cost,
            "description": work.description,
            "start_date": work.start_date,
            "end_date": work.end_date,
            "status": work.status,
            "vehicle_id": work.vehicle_id,
            "created_at": work.created_at,
        }
    except Exception as e:
        logger.error(f"Error fetching work {work_id}: {e}")
        return {"error": "Internal Server Error"}

def create_work(cost, description, start_date, end_date, status, vehicle_id):
    """
    Create a new work entry.
    :param cost: The cost of the work.
    :param description: Description of the work.
    :param start_date: Start date of the work.
    :param end_date: End date of the work.
    :param status: Current status of the work.
    :param vehicle_id: The ID of the associated vehicle.
    :return: dict: A dictionary containing the newly created work's information or an error message.
    """
    try:
        work = Work(
            cost=cost,
            description=description,
            start_date=start_date,
            end_date=end_date,
            status=status,
            vehicle_id=vehicle_id,
        )
        db.session.add(work)
        db.session.commit()
        return {
            "work_id": work.work_id,
            "cost": work.cost,
            "description": work.description,
            "start_date": work.start_date,
            "end_date": work.end_date,
            "status": work.status,
            "vehicle_id": work.vehicle_id,
            "created_at": work.created_at,
        }
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating work: {e}")
        return {"error": "Internal Server Error"}

def update_work(work_id, cost=None, description=None, start_date=None, end_date=None, status=None, vehicle_id=None):
    """
    Update an existing work.
    :param work_id: The ID of the work to update.
    :param cost: The updated cost.
    :param description: The updated description.
    :param start_date: The updated start date.
    :param end_date: The updated end date.
    :param status: The updated status.
    :param vehicle_id: The updated vehicle ID.
    :return: dict: A dictionary containing the updated work's information or an error message.
    """
    try:
        work = Work.query.get(work_id)
        if not work:
            return None

        work.cost = cost if cost is not None else work.cost
        work.description = description if description else work.description
        work.start_date = start_date if start_date else work.start_date
        work.end_date = end_date if end_date else work.end_date
        work.status = status if status else work.status
        work.vehicle_id = vehicle_id if vehicle_id else work.vehicle_id

        db.session.commit()
        return {
            "work_id": work.work_id,
            "cost": work.cost,
            "description": work.description,
            "start_date": work.start_date,
            "end_date": work.end_date,
            "status": work.status,
            "vehicle_id": work.vehicle_id,
            "created_at": work.created_at,
        }
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating work {work_id}: {e}")
        return {"error": "Internal Server Error"}

def delete_work(work_id):
    """
    Delete a work entry.
    :param work_id: The ID of the work to delete.
    :return: dict: A message confirming deletion or an error message.
    """
    try:
        work = Work.query.get(work_id)
        if not work:
            return None
        db.session.delete(work)
        db.session.commit()
        return {"message": f"Work {work_id} deleted successfully"}
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error deleting work {work_id}: {e}")
        return {"error": "Internal Server Error"}
