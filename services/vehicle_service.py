import logging

from models.vehicle import Vehicle
from utils.database import db


logger = logging.getLogger(__name__)

def get_all_vehicle():
    """
    Retrieve all vehicles.
    :return: list: A list of dictionaries containing information about all clients.
    """
    try:
        vehicles = Vehicle.query.all()   # Retrieve all vehicles from the database
        return [
            {
                "vehicle_id": vehicle.vehicle_id,
                "brand": vehicle.brand,
                "model": vehicle.model,
                "license_plate": vehicle.license_plate,
                "year": vehicle.year,
                "client_id": vehicle.client_id,
                "created_at": vehicle.created_at,
            }
            for vehicle in vehicles
        ]
    except Exception as e:
        logger.error(f"Error fetching all vehicles: {e}")
        return {"error": "Internal Server Error"}

def get_vehicle(vehicle_id):
    """
    Retrieve a vehicle by ID.
    :param vehicle_id: The ID of the vehicle to retrieve.
    :return: dict: A dictionary containing the vehicle's information or an error message.
    """
    try:
        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            return None
        return {
            "vehicle_id": vehicle.vehicle_id,
            "brand": vehicle.brand,
            "model": vehicle.model,
            "license_plate": vehicle.license_plate,
            "year": vehicle.year,
            "client_id": vehicle.client_id,
            "created_at": vehicle.created_at,
        }
    except Exception as e:
        logger.error(f"Error fetching vehicle {vehicle_id}: {e}")
        return {"error": "Internal Server Error"}

def create_vehicle(brand, model, license_plate, year, client_id, created_at):
    """
    Create a new vehicle.
    :param brand: The brand of the vehicle.
    :param model: The model of the vehicle.
    :param license_plate: The license plate of the vehicle.
    :param year: The manufacturing year of the vehicle.
    :param client_id: The ID of the client who owns the vehicle.
    :param created_at: Timestamp when the vehicle was created.
    :return: dict: A dictionary containing the newly created vehicle's information or an error message.
    """
    try:
        vehicle = Vehicle(
            brand=brand,
            model=model,
            license_plate=license_plate,
            year=year,
            client_id=client_id,
            created_at=created_at,


        )
        db.session.add(vehicle)  # Save the new vehicle to the database
        db.session.commit()
        return {
            "vehicle_id": vehicle.vehicle_id,
            "brand": vehicle.brand,
            "model": vehicle.model,
            "license_plate": vehicle.license_plate,
            "year": vehicle.year,
            "client_id": vehicle.client_id,
            "created_at": vehicle.created_at,
        }
    except Exception as e:
        logger.error(f"Error creating vehicle: {e}")
        return {"error": "Internal Server Error"}


def update_vehicle(vehicle_id, brand=None, model=None, license_plate=None, year=None, client_id=None, created_at=None):
    """
    Update an existing vehicle.
    :param vehicle_id: The ID of the vehicle to update.
    :param brand: The new brand of the vehicle.
    :param model: The new model of the vehicle.
    :param license_plate: The new license plate of the vehicle.
    :param year: The new year of the vehicle.
    :param client_id: The new client ID of the vehicle.
    :return: dict: A dictionary containing the updated vehicle's information or an error message.
    """
    try:
        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            return None

        # Update the fields if new values are provided
        vehicle.brand = brand if brand else vehicle.brand
        vehicle.model = model if model else vehicle.model
        vehicle.license_plate = license_plate if license_plate else vehicle.license_plate
        vehicle.year = year if year else vehicle.year
        vehicle.client_id = client_id if client_id else vehicle.client_id
        vehicle.created_at = created_at if created_at else vehicle.created_at

        db.session.commit()  # Commit the changes to the database
        return {
            "vehicle_id": vehicle.vehicle_id,
            "brand": vehicle.brand,
            "model": vehicle.model,
            "license_plate": vehicle.license_plate,
            "year": vehicle.year,
            "client_id": vehicle.client_id,
            "created_at": vehicle.created_at,
        }
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        logger.error(f"Error updating vehicle {vehicle_id}: {e}")
        return {"error": "Internal Server Error"}

def delete_vehicle(vehicle_id):
    """
    Delete a vehicle.
    :param vehicle_id: The ID of the vehicle to delete.
    :return: dict: A message confirming deletion or an error message.
    """
    try:
        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            return None
        db.session.delete(vehicle)  # Delete the vehicle
        db.session.commit()
        return {"message": f"Vehicle {vehicle_id} deleted successfully"}
    except Exception as e:
        logger.error(f"Error deleting vehicle {vehicle_id}: {e}")
        return {"error": "Internal Server Error"}