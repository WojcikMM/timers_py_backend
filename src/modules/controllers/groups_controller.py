"""Controller to handling request where target is group_id object"""
from json import loads

from connexion import request, NoContent

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
    created_group = GroupModel(**request.json).save()
    return {'id': str(created_group.id)}, 201


def update_group(group_id: str):
    """ Update the existed group_id
    :param group_id Identity of Group document to update"""
    group: GroupModel = GroupModel.objects.get(id=group_id)
    if group is None:
        return __not_found_response
    else:
        if 'name' in request.json:
            group.name = request.json['name']
        if 'active' in request.json:
            group.active = request.json['active']
        group.save()
        return NoContent, 204


def remove_group_by_id(group_id: str):
    """Delete the existed group_id
    :param group_id -- Identity of the Group document to remove"""
    action: GroupModel = GroupModel.objects.get(id=group_id)
    if action is None:
        return __not_found_response
    delete_return = action.delete()
    print(delete_return)
    return NoContent, 204
