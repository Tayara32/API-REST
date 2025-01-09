import logging
from datetime import datetime

from models.setting import Setting
from utils.database import db

logger = logging.getLogger(__name__)

def get_all_settings():
    """
    Retrieve all settings.
    :return: list: A list of dictionaries containing information about all settings.
    """
    try:
        settings = Setting.query.all()
        return [
            {
                "setting_id": setting.setting_id,
                "key_name": setting.key_name,
                "updated_at": setting.updated_at,
                "value": setting.value,
            }
            for setting in settings
        ]
    except Exception as e:
        logger.error(f"Error fetching all settings: {e}")
        return {"error": "Internal Server Error"}

def get_setting(setting_id):
    """
    Retrieve a setting by ID.
    :param setting_id: The ID of the setting to retrieve.
    :return: dict: A dictionary containing the setting's information or an error message.
    """
    try:
        setting = Setting.query.get(setting_id)
        if not setting:
            return None
        return {
            "setting_id": setting.setting_id,
            "key_name": setting.key_name,
            "updated_at": setting.updated_at,
            "value": setting.value,
        }
    except Exception as e:
        logger.error(f"Error fetching setting {setting_id}: {e}")
        return {"error": "Internal Server Error"}

def create_setting(key_name, updated_at, value):
    """
    Create a new setting entry.
    :param key_name: The key name of the setting.
    :param updated_at: Datetime the setting was last updated.
    :param value: The value of the setting.
    :return: dict: A dictionary containing the newly created setting's information or an error message.
    """
    try:
        setting = Setting(
            key_name=key_name,
            updated_at=updated_at,
            value=value
        )
        db.session.add(setting)
        db.session.commit()
        return {
            "setting_id": setting.setting_id,
            "key_name": setting.key_name,
            "updated_at": setting.updated_at,
            "value": setting.value,
        }
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating setting: {e}")
        return {"error": "Internal Server Error"}

def update_setting(setting_id, key_name=None, updated_at=None, value=None):
    """
    Update an existing setting.
    :param setting_id: The ID of the setting to update.
    :param key_name: The updated key name of the setting.
    :param updated_at: Datetime the setting was last updated.
    :param value: The updated value of the setting.
    :return: dict: A dictionary containing the updated setting's information or an error message.
    """
    try:
        setting = Setting.query.get(setting_id)
        if not setting:
            return None

        setting.key_name = key_name if key_name is not None else setting.key_name
        setting.updated_at = datetime.now()
        setting.value = value if value else setting.value

        db.session.commit()
        return {
            "setting_id": setting.setting_id,
            "key_name": setting.key_name,
            "updated_at": setting.updated_at,
            "value": setting.value,
        }
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating setting {setting_id}: {e}")
        return {"error": "Internal Server Error"}

def delete_setting(setting_id):
    """
    Delete a setting entry.
    :param setting_id: The ID of the setting to delete.
    :return: dict: A message confirming deletion or an error message.
    """
    try:
        setting = Setting.query.get(setting_id)
        if not setting:
            return None
        db.session.delete(setting)
        db.session.commit()
        return {"message": f"Setting {setting_id} deleted successfully"}
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error deleting setting {setting_id}: {e}")
        return {"error": "Internal Server Error"}
