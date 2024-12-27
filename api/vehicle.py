from flask_restx import Namespace, Resource
from services.client_service import get_all_clients, get_client, create_client, update_client, delete_client
from utils.utils import generate_swagger_model
from models.client import Client

# Namespace for clients
clients_ns = Namespace('vehicle', description='CRUD operations for managing clients')

# Generate the Swagger model for clients
client_model = generate_swagger_model(
    api=clients_ns,        # Namespace for which the model is created
    model=Client,          # Database model (SQLAlchemy) used to create the Swagger model
    exclude_fields=[],     # Fields to exclude from the Swagger model
    readonly_fields=['client_id']  # Fields that should be marked as read-only
)