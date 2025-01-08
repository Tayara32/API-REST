import logging
from flask_restx import Namespace, Resource
from werkzeug.exceptions import HTTPException
from services.vehicle_service import (
    get_all_vehicle,
    get_vehicle,
    create_vehicle,
    update_vehicle,
    delete_vehicle
)
from utils.utils import generate_swagger_model
from models.vehicle import Vehicle

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Namespace for managing vehicles
vehicles_ns = Namespace('vehicle', description='CRUD operations for managing vehicles')

# Generate the Swagger model for the vehicle resource
vehicle_model = generate_swagger_model(
    api=vehicles_ns,       # Namespace to associate with the model
    model=Vehicle,         # SQLAlchemy model representing the vehicle resource
    exclude_fields=[],     # No excluded fields in this model
    readonly_fields=['vehicle_id']  # Fields that cannot be modified
)


@vehicles_ns.route('/')
class VehicleList(Resource):
    """
    Handles operations on the collection of vehicles.
    Supports retrieving all vehicles (GET) and creating new vehicles (POST).
    """

    @vehicles_ns.doc('get_all_vehicle')
    @vehicles_ns.marshal_list_with(vehicle_model)
    def get(self):
        """
        Retrieve all vehicles.
        :return: List of all vehicles
        """
        try:
            # Fetch all vehicles from the service layer
            return get_all_vehicle()
        except HTTPException as http_err:
            # Allow HTTP exceptions to propagate their status codes and messages
            logger.error(f"HTTP error while retrieving vehicles: {http_err}")
            raise http_err
        except Exception as e:
            # Log error and return a 500 status code
            logger.error(f"Error retrieving vehicles: {e}")
            vehicles_ns.abort(500, "An error occurred while retrieving the vehicles.")

    @vehicles_ns.doc('create_vehicle')
    @vehicles_ns.expect(vehicle_model, validate=True)
    @vehicles_ns.marshal_with(vehicle_model, code=201)
    def post(self):
        """
        Create a new vehicle.
        :return: The created vehicle with HTTP status code 201
        """
        data = vehicles_ns.payload  # Extract JSON payload
        try:
            # Call the service to create a new vehicle
            return create_vehicle(
                data["brand"], data["model"], data["license_plate"],
                data["year"], data["client_id"], data["created_at"]
            ), 201
        except HTTPException as http_err:
            logger.error(f"HTTP error while creating vehicle: {http_err}")
            raise http_err
        except Exception as e:
            # Log error and return a 500 status code
            logger.error(f"Error creating vehicle: {e}")
            vehicles_ns.abort(500, "An error occurred while creating the vehicle.")


@vehicles_ns.route('/<int:vehicle_id>')
@vehicles_ns.param('vehicle_id', 'The ID of the vehicle')
class Vehicle(Resource):
    """
    Handles operations on a single vehicle.
    Supports retrieving (GET), updating (PUT), and deleting (DELETE) a vehicle.
    """

    @vehicles_ns.doc('get_vehicle')
    @vehicles_ns.marshal_with(vehicle_model)
    def get(self, vehicle_id):
        """
        Retrieve a vehicle by ID.
        :param vehicle_id: The ID of the vehicle
        :return: The vehicle details or 404 if not found
        """
        try:
            # Fetch vehicle by ID
            vehicle = get_vehicle(vehicle_id)
            if not vehicle:
                # Return a 404 error if vehicle does not exist
                vehicles_ns.abort(404, f"Vehicle with ID {vehicle_id} not found.")
            return vehicle
        except HTTPException as http_err:
            logger.error(f"HTTP error while retrieving vehicle with ID {vehicle_id}: {http_err}")
            raise http_err
        except Exception as e:
            # Log error and return a 500 status code
            logger.error(f"Error retrieving vehicle with ID {vehicle_id}: {e}")
            vehicles_ns.abort(500, "An error occurred while retrieving the vehicle.")

    @vehicles_ns.doc('update_vehicle')
    @vehicles_ns.expect(vehicle_model, validate=True)
    @vehicles_ns.marshal_with(vehicle_model)
    def put(self, vehicle_id):
        """
        Update a vehicle by ID.
        :param vehicle_id: The ID of the vehicle
        :return: The updated vehicle details or 404 if not found
        """
        data = vehicles_ns.payload  # Extract JSON payload
        try:
            # Call the service to update the vehicle
            vehicle = update_vehicle(
                vehicle_id, data.get("brand"), data.get("model"), data.get("license_plate"),  data.get("year"), data.get("client_id")
            )
            if not vehicle:
                # Return a 404 error if vehicle does not exist
                vehicles_ns.abort(404, f"Vehicle with ID {vehicle_id} not found.")
            return vehicle
        except HTTPException as http_err:
            logger.error(f"HTTP error while updating vehicle with ID {vehicle_id}: {http_err}")
            raise http_err
        except Exception as e:
            # Log error and return a 500 status code
            logger.error(f"Error updating vehicle with ID {vehicle_id}: {e}")
            vehicles_ns.abort(500, "An error occurred while updating the vehicle.")

    @vehicles_ns.doc('delete_vehicle')
    @vehicles_ns.response(204, 'Vehicle successfully deleted')
    def delete(self, vehicle_id):
        """
        Delete a vehicle by ID.
        :param vehicle_id: The ID of the vehicle
        :return: HTTP 204 status code if deleted successfully or 404 if not found
        """
        try:
            # Call the service to delete the vehicle
            vehicle = delete_vehicle(vehicle_id)
            if not vehicle:
                # Return a 404 error if vehicle does not exist
                vehicles_ns.abort(404, f"Vehicle with ID {vehicle_id} not found.")
            return '', 204  # Return no content with status code 204
        except HTTPException as http_err:
            logger.error(f"HTTP error while deleting vehicle with ID {vehicle_id}: {http_err}")
            raise http_err
        except Exception as e:
            # Log error and return a 500 status code
            logger.error(f"Error deleting vehicle with ID {vehicle_id}: {e}")
            vehicles_ns.abort(500, "An error occurred while deleting the vehicle.")
