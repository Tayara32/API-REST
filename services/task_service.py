import logging
from models.task import Task
from utils.database import db

logger = logging.getLogger(__name__)

def get_all_task():
    """
    Retrieve all tasks.
    :return: list: A list of dictionaries containing information about all tasks.
    """
    try:
        tasks = Task.query.all()
        return [
            {
                "task_id": task.task_id,
                "description": task.description,
                "status": task.status,
                "start_date": task.start_date,
                "end_date": task.end_date,
                "created_at": task.created_at,
                "work_id": task.work_id,
                "employee_id": task.employee_id,
            }
            for task in tasks
        ]
    except Exception as e:
        logger.error(f"Error fetching all tasks: {e}")
        return {"error": "Internal Server Error"}

def get_task(task_id):
    """
    Retrieve a task by ID.
    :param task_id: The ID of the task to retrieve.
    :return: dict: A dictionary containing the task's information or an error message.
    """
    try:
        task = Task.query.get(task_id)
        if not task:
            return None
        return {
            "task_id": task.task_id,
            "description": task.description,
            "status": task.status,
            "start_date": task.start_date,
            "end_date": task.end_date,
            "created_at": task.created_at,
            "work_id": task.work_id,
            "employee_id": task.employee_id,
        }
    except Exception as e:
        logger.error(f"Error fetching task {task_id}: {e}")
        return {"error": "Internal Server Error"}

def create_task(description, status, start_date, end_date, work_id, employee_id):
    """
    Create a new task entry.
    :param description: Description of the task.
    :param status: The current status of the task.
    :param start_date: Start date of the task.
    :param end_date: End date of the task.
    :param work_id: The ID of the associated work.
    :param employee_id: The ID of the associated employee.
    :return: dict: A dictionary containing the newly created task's information or an error message.
    """
    try:
        task = Task(
            description=description,
            status=status,
            start_date=start_date,
            end_date=end_date,
            work_id=work_id,
            employee_id=employee_id,
        )
        db.session.add(task)
        db.session.commit()
        return {
            "task_id": task.task_id,
            "description": task.description,
            "status": task.status,
            "start_date": task.start_date,
            "end_date": task.end_date,
            "created_at": task.created_at,
            "work_id": task.work_id,
            "employee_id": task.employee_id,
        }
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating task: {e}")
        return {"error": "Internal Server Error"}

def update_task(task_id, description=None, status=None, start_date=None, end_date=None, work_id=None, employee_id=None):
    """
    Update an existing task.
    :param task_id: The ID of the task to update.
    :param description: The updated description.
    :param status: The updated status.
    :param start_date: The updated start date.
    :param end_date: The updated end date.
    :param work_id: The updated work ID.
    :param employee_id: The updated employee ID.
    :return: dict: A dictionary containing the updated task's information or an error message.
    """
    try:
        task = Task.query.get(task_id)
        if not task:
            return None

        task.description = description if description else task.description
        task.status = status if status else task.status
        task.start_date = start_date if start_date else task.start_date
        task.end_date = end_date if end_date else task.end_date
        task.work_id = work_id if work_id else task.work_id
        task.employee_id = employee_id if employee_id else task.employee_id

        db.session.commit()
        return {
            "task_id": task.task_id,
            "description": task.description,
            "status": task.status,
            "start_date": task.start_date,
            "end_date": task.end_date,
            "created_at": task.created_at,
            "work_id": task.work_id,
            "employee_id": task.employee_id,
        }
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating task {task_id}: {e}")
        return {"error": "Internal Server Error"}

def delete_task(task_id):
    """
    Delete a task entry.
    :param task_id: The ID of the task to delete.
    :return: dict: A message confirming deletion or an error message.
    """
    try:
        task = Task.query.get(task_id)
        if not task:
            return None
        db.session.delete(task)
        db.session.commit()
        return {"message": f"Task {task_id} deleted successfully"}
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error deleting task {task_id}: {e}")
        return {"error": "Internal Server Error"}
