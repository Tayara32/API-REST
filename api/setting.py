import logging
from flask_restx import Namespace, Resource
from werkzeug.exceptions import HTTPException
from services.setting_service import (
    get_all_settings,
    get_setting,
    create_setting,
    update_setting,
    delete_setting
)
from utils.utils import generate_swagger_model
from models.setting import Setting

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Namespace for managing setting
settings_ns = Namespace('setting', updated_at='CRUD operations for managing settings')

# Generate the Swagger model for the setting resource
setting_model = generate_swagger_model(
    api=settings_ns,       # Namespace to associate with the model
    model=Setting,        # SQLAlchemy model representing the setting resource
    exclude_fields=[], # No excluded fields in this model
    readonly_fields=['setting_id']  # Fields that cannot be modified
)


@settings_ns.route('/')
class InvoiceItemList(Resource):
    """
    Handles operations on the collection of settings.
    Supports retrieving all settings (GET) and creating new settings (POST).
    """

    @settings_ns.doc('get_all_settings')
    @settings_ns.marshal_list_with(setting_model)
    def get(self):
        """
        Retrieve all settings.
        :return: List of all settings
        """
        try:
            return get_all_settings()
        except HTTPException as http_err:
            logger.error(f"HTTP error while retrieving settings: {http_err}")
            raise http_err
        except Exception as e:
            logger.error(f"Error retrieving settings: {e}")
            settings_ns.abort(500, "An error occurred while retrieving the settings.")

    @settings_ns.doc('create_setting')
    @settings_ns.expect(setting_model, validate=True)
    @settings_ns.marshal_with(setting_model, code=201)
    def post(self):
        """
        Create a new setting.
        :return: The created setting with HTTP status code 201
        """
        data = settings_ns.payload
        try:
            return create_setting(
                data["key_name"], data["updated_at"], data["value"]
            ), 201
        except HTTPException as http_err:
            logger.error(f"HTTP error while creating setting: {http_err}")
            raise http_err
        except Exception as e:
            logger.error(f"Error creating setting: {e}")
            settings_ns.abort(500, "An error occurred while creating the setting.")


@settings_ns.route('/<int:setting_id>')
@settings_ns.param('setting_id', 'The ID of the setting.')
class InvoiceItemResource(Resource):
    """
    Handles operations on a single setting.
    Supports retrieving (GET), updating (PUT), and deleting (DELETE) an setting.
    """

    @settings_ns.doc('get_setting')
    @settings_ns.marshal_with(setting_model)
    def get(self, setting_id):
        """
        Retrieve an setting by ID.
        :param setting_id: The ID of the setting
        :return: The setting details or 404 if not found
        """
        try:
            setting = get_setting(setting_id)
            if not setting:
                settings_ns.abort(404, f"setting with ID {setting_id} not found.")
            return setting
        except HTTPException as http_err:
            logger.error(f"HTTP error while retrieving setting with ID {setting_id}: {http_err}")
            raise http_err
        except Exception as e:
            logger.error(f"Error retrieving setting with ID {setting_id}: {e}")
            settings_ns.abort(500, "An error occurred while retrieving the setting.")

    @settings_ns.doc('update_setting')
    @settings_ns.expect(setting_model, validate=True)
    @settings_ns.marshal_with(setting_model)
    def put(self, setting_id):
        """
        Update an setting by ID.
        :param setting_id: The ID of the setting
        :return: The updated setting details or 404 if not found
        """
        data = settings_ns.payload
        try:
            setting = update_setting(
                setting_id, data.get("key_name"), data.get("updated_at"),
                data.get("value")
            )
            if not setting:
                settings_ns.abort(404, f"setting with ID {setting_id} not found.")
            return setting
        except HTTPException as http_err:
            logger.error(f"HTTP error while updating setting with ID {setting_id}: {http_err}")
            raise http_err
        except Exception as e:
            logger.error(f"Error updating setting with ID {setting_id}: {e}")
            settings_ns.abort(500, "An error occurred while updating the setting.")

    @settings_ns.doc('delete_setting')
    @settings_ns.response(204, 'setting successfully deleted')
    def delete(self, setting_id):
        """
        Delete a setting by ID.
        :param setting_id: The ID of the setting
        :return: HTTP 204 status code if deleted successfully or 404 if not found
        """
        try:
            setting = delete_setting(setting_id)
            if not setting:
                settings_ns.abort(404, f"setting with ID {setting_id} not found.")
            return '', 204
        except HTTPException as http_err:
            logger.error(f"HTTP error while deleting setting with ID {setting_id}: {http_err}")
            raise http_err
        except Exception as e:
            logger.error(f"Error deleting setting with ID {setting_id}: {e}")
            settings_ns.abort(500, "An error occurred while deleting the setting.")
