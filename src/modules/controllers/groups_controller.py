"""Controller to handling request where target is group object"""
from connexion import request, NoContent
from injector import inject

from modules.abstracts.database.collection_providers.collection_providers_abstract import \
    GroupsCollectionProviderAbstract


@inject
def get_all_groups(provider: GroupsCollectionProviderAbstract):
    """
    Returns all groups from database
    :return: list of group documents
    """
    return provider.get_all_documents(), 200


@inject
def get_group(group_id: str, provider: GroupsCollectionProviderAbstract):
    """Get group by group identity
    :param provider: Abstract declaration of GroupsCollectionProvider
    :param group_id identity of specific group
    """
    return provider.get_document_by_id(group_id), 200


@inject
def create_group(provider: GroupsCollectionProviderAbstract,**kwargs):
    """Create new group
    :param provider: Abstract declaration of GroupsCollectionProvider
    """
    print(kwargs)
    return provider.insert_document(request.json), 201


@inject
def update_group(group_id: str, provider: GroupsCollectionProviderAbstract):
    """ Update the existed group
    :param group_id identity of group to update
    :param provider: Abstract declaration of GroupsCollectionProvider
    """
    body = request.json
    updated_id = provider.update_document_by_id(group_id, body)
    status_code = 404 if updated_id is None else 200
    return NoContent, status_code


@inject
def delete_group(group_id: str, provider: GroupsCollectionProviderAbstract):
    """Delete the existed group
    :param provider: Abstract declaration of GroupsCollectionProvider
    :param group_id -- Identity of the group to remove"""
    status_code = 404 if provider.delete_document_by_id(group_id) is None else 204
    return NoContent, status_code
