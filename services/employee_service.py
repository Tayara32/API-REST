import logging
from models.employee import Employee
from flask_restx import abort

logger = logging.getLogger(__name__)

def get_all_employees():
    """
    Retrieve all employees.
    :return: dict: A list of dictionaries containing employee information.
    """
    try:
        employees = Employee.query.all()
        return [{"employee_id": employee.employee_id, "name": employee.name, "email": employee.email, "phone": employee.phone, "role": employee.role, "hired_date": employee.hired_date, "created_at": employee.created_at} for employee in employees]
    except Exception as e:
        logger.error(f"Error fetching all employees: {e}")
        return {"error": "Internal Server Error"}, 500

def get_employee(employee_id):
    """
    Retrieve an employee by ID.
    :param employee_id: The ID of the employee to retrieve.
    :return: dict: A dictionary containing the employee's information or None if not found.
    """
    try:
        # Query the database for the employee by ID
        employee = Employee.query.get(employee_id)
        if not employee:
            return None  # Return None if the employee is not found
        # Return employee data as a dictionary
        return {
            "employee_id": employee.employee_id,
            "name": employee.name,
            "email": employee.email,
            "phone": employee.phone,
            "role": employee.role,
            "hired_date": employee.hired_date,
            "created_at": employee.created_at,
        }
    except Exception as e:
        logger.error(f"Error fetching employee {employee_id}: {e}")
        raise  # Raise the exception to let the API layer handle it

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
            return {"error": f"Employee with ID {employee_id} not found."}, 404
        employee.name = name
        employee.email = email
        employee.phone = phone
        employee.role = role
        employee.hired_date = hired_date
        employee.save()  # Save the updated employee to the database
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
            return {"error": f"Employee with ID {employee_id} not found."}, 404
        employee.delete()  # Delete the employee from the database
        return {"message": f"Employee with ID {employee_id} deleted."}, 204
    except Exception as e:
        logger.error(f"Error deleting employee {employee_id}: {e}")
        return {"error": "Internal Server Error"}, 500

