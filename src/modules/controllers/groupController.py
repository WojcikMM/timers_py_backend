"""Controller to handling request where target is group object"""
from connexion import request, NoContent
from modules.database.providers.groups_collection_provider import GroupsCollectionProvider


def get_all_groups() -> None:
    """
    Returns all groups from database
    :return: list of group documents
    """
    return GroupsCollectionProvider().get_all_documents(), 200


def get_group(group_id: str) -> None:
    """Get group by group identity
    :param group_id identity of specific group
    """
    return GroupsCollectionProvider().get_document_by_id(group_id), 200


def create_group() -> None:
    """Create new group"""
    body = request.json
    print(body)
    return GroupsCollectionProvider().insert_document(body), 201


def update_group(group_id: str) -> None:
    """ Update the existed group
    :param group_id identity of group to update
    """
    body = request.json
    updated_id = GroupsCollectionProvider().update_document_by_id(group_id, body)
    status_code = 404 if updated_id is None else 200
    return NoContent, status_code


def delete_group(group_id: str) -> None:
    """Delete the existed group
    :param group_id -- Identity of the group to remove"""
    status_code = 404 if GroupsCollectionProvider().delete_document_by_id(group_id) is None else 204
    return NoContent, status_code
