"""Controller to handling request where target is action object"""
from connexion import request, NoContent
from modules.abstracts.database.collection_providers.collection_providers_abstract import \
    ActionsCollectionProviderAbstract
from injector import inject

from modules.attributes.authorize import Authorize


@inject
def get_all_actions(actions_provider: ActionsCollectionProviderAbstract) -> {any, int}:
    """
    Returns all actions from database
    :type actions_provider: Abstract class - need to override in binding options
    :return: list of action documents
    """
    return actions_provider.get_all_documents(), 200


@inject
def get_action(action_id: str, actions_provider: ActionsCollectionProviderAbstract) -> None:
    """Get action by action identity
    :param actions_provider: Abstract class - need to override in binding options
    :param action_id identity of specific action
    """
    return actions_provider.get_document_by_id(action_id), 200


@inject
def create_action(actions_provider: ActionsCollectionProviderAbstract) -> None:
    """Create new action
    :type actions_provider: Abstract class - need to override in binding options
    """
    body = request.json
    print(body)
    return actions_provider.insert_document(body), 201


@inject
def update_action(action_id: str, actions_provider: ActionsCollectionProviderAbstract) -> None:
    """ Update the existed action
    :param actions_provider: Abstract class - need to override in binding options
    :param action_id identity of action to update
    """
    updated_id = actions_provider.update_document_by_id(action_id, request.json)
    status_code = 404 if updated_id is None else 200
    return NoContent, status_code


@inject
@Authorize('ADMIN')
def delete_action(action_id: str, actions_provider: ActionsCollectionProviderAbstract, token_info) -> None:
    """Delete the existed action
    :param actions_provider: Abstract class - need to override in binding options
    :param action_id -- Identity of the action to remove"""
    print(type(token_info))
    status_code = 404 if actions_provider.delete_document_by_id(action_id) is None else 204
    return NoContent, status_code
