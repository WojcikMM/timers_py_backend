from src.modules.database.main.main_db import MainDatabase
from src.modules.database.actions_collection import ActionCollection
from src.config import database_settings
from connexion import request, NoContent

main_database = MainDatabase(database_settings['connection_string'], database_settings['database_name'])
action_collection = ActionCollection(main_database)


def get_all_actions() -> None:
    """
    Returns all actions from database
    :return: list of action documents
    """
    return action_collection.get_all_actions(), 200


def get_action(action_id: str) -> None:
    """Get action by action identity
    :param action_id identity of specific action
    """
    return action_collection.get_action_by_id(action_id), 200


def create_action() -> None:
    """Create new action"""
    body = request.json
    print(body)
    new_document_id = action_collection.create_action(body)
    return new_document_id, 201


def update_action(action_id: str) -> None:
    """ Update the existed action
    :param action_id identity of action to update
    """
    body = request.json
    updated_id = action_collection.update_action(action_id, body)

    if updated_id is not None:
        return NoContent, 200
    else:
        return NoContent, 404


def delete_action(action_id: str) -> None:
    """Delete the existed action
    :param action_id -- Identity of the action to remove"""
    result = action_collection.delete_action(action_id)
    if result is not None:
        return NoContent, 204
    else:
        return NoContent, 404
