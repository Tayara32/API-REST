import logging
from models.client import Client

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_all_clients():
    """
    Retrieve all clients.
    :return: dict: A dictionary containing information about all clients.
    """
    try:
        clients = Client.query.all()  # Retrieve all clients from the database
        logger.info(f"Retrieved {len(clients)} clients.")
        return [{"client_id": client.client_id, "name": client.name, "email": client.email, "phone": client.phone, "address": client.address, "created_at": client.created_at} for client in clients]
    except Exception as e:
        logger.error(f"Error fetching all clients: {e}")
        return {"error": "Internal Server Error"}, 500

def get_client(client_id):
    """
    Retrieve a client by ID.
    :param client_id: The ID of the client to retrieve.
    :return: dict: A dictionary containing the client's information.
    """
    try:
        client = Client.query.get(client_id)
        if not client:
            logger.warning(f"Client with ID {client_id} not found.")
            return {"error": f"Client with ID {client_id} not found."}, 404
        return {"client_id": client.client_id, "name": client.name, "email": client.email, "phone": client.phone, "address": client.address, "created_at": client.created_at}
    except Exception as e:
        logger.error(f"Error fetching client {client_id}: {e}")
        return {"error": "Internal Server Error"}, 500

def create_client(name, email, phone, address):
    """
    Create a new client.
    :param name: The name of the client.
    :param email: The email of the client.
    :param phone: The phone number of the client.
    :param address: The address of the client.
    :return: dict: A dictionary containing the newly created client's information.
    """
    try:
        client = Client(name=name, email=email, phone=phone, address=address)
        client.save()  # Save the new client to the database
        logger.info(f"Created new client with ID {client.client_id}.")
        return {"client_id": client.client_id, "name": client.name, "email": client.email, "phone": client.phone, "address": client.address, "created_at": client.created_at}, 201
    except Exception as e:
        logger.error(f"Error creating client: {e}")
        return {"error": "Internal Server Error"}, 500

def update_client(client_id, name, email, phone, address):
    """
    Update an existing client.
    :param client_id: The ID of the client to update.
    :param name: The new name of the client.
    :param email: The new email of the client.
    :param phone: The new phone number of the client.
    :param address: The new address of the client.
    :return: dict: A dictionary containing the updated client's information.
    """
    try:
        client = Client.query.get(client_id)
        if not client:
            logger.warning(f"Client with ID {client_id} not found for update.")
            return {"error": f"Client with ID {client_id} not found."}, 404
        client.name = name
        client.email = email
        client.phone = phone
        client.address = address
        client.save()  # Save the updated client to the database
        logger.info(f"Updated client with ID {client_id}.")
        return {"client_id": client.client_id, "name": client.name, "email": client.email, "phone": client.phone, "address": client.address, "created_at": client.created_at}
    except Exception as e:
        logger.error(f"Error updating client {client_id}: {e}")
        return {"error": "Internal Server Error"}, 500

def delete_client(client_id):
    """
    Delete a client.
    :param client_id: The ID of the client to delete.
    :return: dict: A dictionary containing the deleted client's information.
    """
    try:
        client = Client.query.get(client_id)
        if not client:
            logger.warning(f"Client with ID {client_id} not found for deletion.")
            return {"error": f"Client with ID {client_id} not found."}, 404
        client.delete()  # Delete the client from the database
        logger.info(f"Deleted client with ID {client_id}.")
        return {"message": f"Client with ID {client_id} deleted."}, 204
    except Exception as e:
        logger.error(f"Error deleting client {client_id}: {e}")
        return {"error": "Internal Server Error"}, 500