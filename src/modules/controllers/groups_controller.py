"""Controller to handling request where target is group_id object"""
from json import loads
from operator import itemgetter

from connexion import request, NoContent
from injector import inject
from modules.database.models import GroupModel

__not_found_response = {'messaage': 'No groups found'}, 404


def get_all_groups():
    """Returns all groups from database"""
    return loads(GroupModel.objects().to_json()), 200


def get_group_by_id(group_id: str):
    """Get Group by group_id identity
    :param group_id identity of specific Group"""
    action = GroupModel.objects.get(id=group_id)
    if action is None:
        return __not_found_response
    return loads(action.to_json()), 200


def create_group():
    """Create new Group document"""
    return {'id': GroupModel(**request.json).save().id}, 201


def update_group(group_id: str):
    """ Update the existed group_id
    :param group_id Identity of Group document to update"""
    action: GroupModel = GroupModel.objects.get(id=group_id)
    if action is None:
        return __not_found_response
    else:
        name, active = itemgetter('name', 'active')(request.json)
        if name is not None:
            action.name = name
        if active is not None:
            action.active = active
        action.save()
        return NoContent, 204


@inject
def remove_group_by_id(group_id: str):
    """Delete the existed group_id
    :param group_id -- Identity of the Group document to remove"""
    action: GroupModel = GroupModel.objects.get(id=group_id)
    if action is None:
        return __not_found_response
    delete_return = action.delete()
    print(delete_return)
    return NoContent, 204
