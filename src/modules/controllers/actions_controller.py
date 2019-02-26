"""Controller to handling request where target is action object"""
from json import loads

from connexion import request, NoContent

from modules.database.models import ActionModel, GroupModel

__not_found_response = {'messaage': 'No actions found'}, 404


def get_all_actions() -> {any, int}:
    """
    Returns all actions from database
    :return: list of action documents
    """
    actions = ActionModel.objects()
    if len(actions) == 0:
        return __not_found_response
    return loads(actions.to_json()), 200


def get_action_by_id(action_id: str):
    """Get action by action identity
    :param action_id identity of specific action
    """
    action = ActionModel.objects.get(id=action_id)
    return loads(action.to_json()), 200


def get_actions_for_group(group_id: str):
    """Get actions by related GroupModel identity
    :param group_id identity of related group_id document
    """
    actions = ActionModel.objects(group_id=group_id)
    if len(actions) == 0:
        return __not_found_response
    return loads(actions.to_json()), 200


def create_action():
    """Create new action"""
    created_action = ActionModel(**request.json).save()
    return {'id': str(created_action.id)}, 201


def update_action(action_id: str):
    """ Update the existed action
    :param action_id identity of action to update
    """
    action: ActionModel = ActionModel.objects.get(id=action_id)
    if action is None:
        return __not_found_response
    else:
        if 'group_id' in request.json:
            action.group_id = GroupModel.objects.get(id=request.json['group_id'])
        if 'name' in request.json:
            action.name = request.json['name']
        if 'active' in request.json:
            action.active = request.json['active']
        action.save()
        return NoContent, 204


def remove_action_by_id(action_id: str, token_info: dict):
    """Delete the existed action
    :param action_id -- Identity of the action to remove"""
    print(type(token_info), token_info)
    action: ActionModel = ActionModel.objects.get(id=action_id)
    if action is None:
        return __not_found_response
    delete_return = action.delete()
    print(delete_return)
    return NoContent, 204
