"""Controller to handling request where target is action object"""
from operator import itemgetter
from connexion import request, NoContent
from modules.database.models import ActionModel
from json import loads

__not_found_response = {'messaage': 'No actions found'}, 404


def get_all_actions() -> {any, int}:
    """
    Returns all actions from database
    :return: list of action documents
    """
    return loads(ActionModel.objects().to_json()), 200


def get_action_by_id(action_id: str):
    """Get action by action identity
    :param action_id identity of specific action
    """
    action = ActionModel.objects.get(id=action_id)
    if action is None:
        return __not_found_response
    return loads(action.to_json()), 200


def get_actions_for_group(group_id: str):
    """Get actions by related GroupModel identity
    :param group_id identity of related group_id document
    """
    actions = ActionModel.objects(group=group_id, active=True)
    if actions is not None:
        return __not_found_response
    return loads(actions.to_json()), 200


def create_action():
    """Create new action"""
    return {'id': ActionModel(**request.json).save().id}, 201


def update_action(action_id: str):
    """ Update the existed action
    :param action_id identity of action to update
    """
    action: ActionModel = ActionModel.objects.get(id=action_id)
    if action is None:
        return __not_found_response
    else:
        group_id, name, active = itemgetter('group_id', 'name', 'active')(request.json)
        if group_id is not None:
            action.group_id = group_id
        if name is not None:
            action.name = name
        if active is not None:
            action.active = active
        action.save()
        return NoContent, 204


def remove_action_by_id(action_id: str, token_info) -> None:
    """Delete the existed action
    :param action_id -- Identity of the action to remove"""
    print(type(token_info))
    action: ActionModel = ActionModel.objects.get(id=action_id)
    if action is None:
        return __not_found_response
    delete_return = action.delete()
    print(delete_return)
    return NoContent, 204
