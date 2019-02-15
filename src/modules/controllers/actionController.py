"""Controller to handling request where target is action object"""
from connexion import request, NoContent
from modules.database.providers.actions_collection_provider import ActionsCollectionProvider


def get_all_actions() -> None:
    """
    Returns all actions from database
    :return: list of action documents
    """
    return ActionsCollectionProvider().get_all_documents(), 200


def get_action(action_id: str) -> None:
    """Get action by action identity
    :param action_id identity of specific action
    """
    return ActionsCollectionProvider().get_document_by_id(action_id), 200


def create_action() -> None:
    """Create new action"""
    body = request.json
    print(body)
    return ActionsCollectionProvider().insert_document(body), 201


def update_action(action_id: str) -> None:
    """ Update the existed action
    :param action_id identity of action to update
    """
    body = request.json
    print(body)
    updated_id = ActionsCollectionProvider().update_document_by_id(action_id, body)

    status_code = 404 if updated_id is None else 200
    return NoContent, status_code


def delete_action(action_id: str) -> None:
    """Delete the existed action
    :param action_id -- Identity of the action to remove"""
    status_code = 404 if ActionsCollectionProvider().delete_document_by_id(action_id) is None else 204
    return NoContent, status_code
