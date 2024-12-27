import logging
from models.employee import Employee

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_all_employees():
    """
    Retrieve all employees.
    :return: dict: A list of dictionaries containing employee information.
    """
    try:
        employees = Employee.query.all()

        # Log custom info about employee retrieval
        logger.info(f"Function 'get_all_employees' executed successfully. Retrieved {len(employees)} employees.")
        return [{"employee_id": employee.employee_id, "name": employee.name, "email": employee.email, "phone": employee.phone, "role": employee.role, "hired_date": employee.hired_date, "created_at": employee.created_at} for employee in employees]
    except Exception as e:
        logger.error(f"Error fetching all employees: {e}")
        return {"error": "Internal Server Error"}, 500

def get_employee(employee_id):
    """
    Retrieve an employee by ID.
    :param employee_id: The ID of the employee to retrieve.
    :return: dict: A dictionary containing the employee's information.
    """
    try:
        employee = Employee.query.get(employee_id)
        if not employee:
            logger.warning(f"Employee with ID {employee_id} not found.")
            return {"error": f"Employee with ID {employee_id} not found."}, 404
        logger.info(f"Retrieved employee with ID {employee_id}.")
        return {"employee_id": employee.employee_id, "name": employee.name, "email": employee.email, "phone": employee.phone, "role": employee.role, "hired_date": employee.hired_date, "created_at": employee.created_at}
    except Exception as e:
        logger.error(f"Error fetching employee {employee_id}: {e}")
        return {"error": "Internal Server Error"}, 500

def create_employee(name, email, phone, role, hired_date):
    """
    Create a new employee.
    :param name: The name of the employee.
    :param email: The email of the employee.
    :param phone: The phone number of the employee.
    :param role: The role of the employee.
    :param hired_date: The date the employee was hired.
    :return: dict: A dictionary containing the created employee's information.
    """
    try:
        employee = Employee(name=name, email=email, phone=phone, role=role, hired_date=hired_date)
        employee.save()  # Save the new employee to the database
        logger.info(f"Created new employee with ID {employee.employee_id}.")
        return {"employee_id": employee.employee_id, "name": employee.name, "email": employee.email, "phone": employee.phone, "role": employee.role, "hired_date": employee.hired_date, "created_at": employee.created_at}, 201
    except Exception as e:
        logger.error(f"Error creating employee: {e}")
        return {"error": "Internal Server Error"}, 500

def update_employee(employee_id, name, email, phone, role, hired_date):
    """
    Update an employee's information.
    :param employee_id: The ID of the employee to update.
    :param name: The name of the employee.
    :param email: The email of the employee.
    :param phone: The phone number of the employee.
    :param role: The role of the employee.
    :param hired_date: The date the employee was hired.
    :return: dict: A dictionary containing the updated employee's information.
    """
    try:
        employee = Employee.query.get(employee_id)
        if not employee:
            logger.warning(f"Employee with ID {employee_id} not found for update.")
            return {"error": f"Employee with ID {employee_id} not found."}, 404
        employee.name = name
        employee.email = email
        employee.phone = phone
        employee.role = role
        employee.hired_date = hired_date
        employee.save()  # Save the updated employee to the database
        logger.info(f"Updated employee with ID {employee_id}.")
        return {"employee_id": employee.employee_id, "name": employee.name, "email": employee.email, "phone": employee.phone, "role": employee.role, "hired_date": employee.hired_date, "created_at": employee.created_at}
    except Exception as e:
        logger.error(f"Error updating employee {employee_id}: {e}")
        return {"error": "Internal Server Error"}, 500

def delete_employee(employee_id):
    """
    Delete an employee.
    :param employee_id: The ID of the employee to delete.
    :return: dict: A dictionary containing the deleted employee's information.
    """
    try:
        employee = Employee.query.get(employee_id)
        if not employee:
            logger.warning(f"Employee with ID {employee_id} not found for deletion.")
            return {"error": f"Employee with ID {employee_id} not found."}, 404
        employee.delete()  # Delete the employee from the database
        logger.info(f"Deleted employee with ID {employee_id}.")
        return {"message": f"Employee with ID {employee_id} deleted."}, 204
    except Exception as e:
        logger.error(f"Error deleting employee {employee_id}: {e}")
        return {"error": "Internal Server Error"}, 500

