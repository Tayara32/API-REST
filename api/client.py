from flask_restx import Namespace, Resource
from services.client_service import get_all_clients, get_client, create_client, update_client, delete_client
from utils.utils import generate_swagger_model
from models.client import Client
import logging

# Namespace for clients
clients_ns = Namespace('client', description='CRUD operations for managing clients')

# Generate the Swagger model for clients
client_model = generate_swagger_model(
    api=clients_ns,        # Namespace for which the model is created
    model=Client,          # Database model (SQLAlchemy) used to create the Swagger model
    exclude_fields=[],     # Fields to exclude from the Swagger model
    readonly_fields=['client_id']  # Fields that should be marked as read-only
)
# Routes for managing clients
@clients_ns.route('/')
class ClientList(Resource):
    """
    Resource for operations on the collection of clients (GET all, POST new).
    """

    @clients_ns.doc('get_all_clients')  # Swagger documentation tag for getting all clients
    @clients_ns.marshal_list_with(client_model)  # Specifies the response format using the Swagger model
    def get(self):
        """
        Get all clients.
        :return: List of all clients in dictionary format
        """
        try:
            return get_all_clients()
        except Exception as e:
            logger.error(f"Error getting all clients: {e}")
            clients_ns.abort(500, "An error occurred while retrieving the clients.")

    @clients_ns.doc('create_client')  # Swagger documentation tag for creating a new client
    @clients_ns.expect(client_model, validate=True)  # Validates the incoming payload against the Swagger model
    @clients_ns.marshal_with(client_model, code=201)  # Specifies the response format for the created client
    def post(self):
        """
        Create a new client.
        :return: Dictionary of the created client with HTTP 201 status code
        """
        data = clients_ns.payload  # Incoming JSON payload
        try:
            return create_client(data), 201
        except Exception as e:
            logger.error(f"Error creating client: {e}")
            clients_ns.abort(500, "An error occurred while creating the client.")


@clients_ns.route('/<int:client_id>')
@clients_ns.param('client_id', 'The Client ID')  # Describes the path parameter
class Client(Resource):
    """
    Resource for operations on a single client (GET, PUT, DELETE).
    """

    @clients_ns.doc('get_client_by_id')  # Swagger documentation tag for retrieving a client by ID
    @clients_ns.marshal_with(client_model)  # Specifies the response format using the Swagger model
    def get(self, client_id):
        """
        Get a client by ID.
        :param client_id: The ID of the client
        :return: Dictionary of the client or a 404 error if not found
        """
        try:
            client = get_client(client_id)
            if not client:
                clients_ns.abort(404, f"Client with ID {client_id} not found.")
            return client
        except Exception as e:
            logger.error(f"Error getting client by ID {client_id}: {e}")
            clients_ns.abort(500, "An error occurred while retrieving the client.")

    @clients_ns.doc('update_client')  # Swagger documentation tag for updating a client
    @clients_ns.expect(client_model, validate=True)  # Validates the incoming payload against the Swagger model
    @clients_ns.marshal_with(client_model)  # Specifies the response format for the updated client
    def put(self, client_id):
        """
        Update a client.
        :param client_id: The ID of the client
        :return: Dictionary of the updated client or a 404 error if not found
        """
        data = clients_ns.payload  # Incoming JSON payload
        try:
            client = update_client(client_id, data)
            if not client:
                clients_ns.abort(404, f"Client with ID {client_id} not found.")
            return client
        except Exception as e:
            logger.error(f"Error updating client with ID {client_id}: {e}")
            clients_ns.abort(500, "An error occurred while updating the client.")

    @clients_ns.doc('delete_client')  # Swagger documentation tag for deleting a client
    @clients_ns.response(204, 'Client successfully deleted')  # Response code for successful deletion
    def delete(self, client_id):
        """
        Delete a client.
        :param client_id: The ID of the client
        :return: Empty response body with HTTP 204 status code or a 404 error if not found
        """
        try:
            client = delete_client(client_id)
            if not client:
                clients_ns.abort(404, f"Client with ID {client_id} not found.")
            return '', 204  # Return no content with status code 204
        except Exception as e:
            logger.error(f"Error deleting client with ID {client_id}: {e}")
            clients_ns.abort(500, "An error occurred while deleting the client.")