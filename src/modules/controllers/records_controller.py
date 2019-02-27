"""Controller to handling request where target is record object"""
from json import loads
from connexion import request, NoContent
from modules.database.models import RecordModel, UserModel, ActionModel, GroupModel

__not_found_response = {'messaage': 'No Records found'}, 404


def get_all_records():
    """Returns all Records from database"""
    return loads(RecordModel.objects().to_json()), 200


def get_user_records(login: str):
    user_id = UserModel.objects.get(login=login).id
    return loads(RecordModel.objects(user_id=user_id).to_json()), 200


def get_own_records(user: str):
    user_id = UserModel.objects.get(login=user).id
    return loads(RecordModel.objects(user_id=user_id).to_json()), 200


def get_record_by_id(record_id: str):
    """Get Record document by record_id identity
    :param record_id identity of specific Record"""
    record = RecordModel.objects.get(id=record_id)
    if record is None:
        return __not_found_response
    return loads(record.to_json()), 200


def get_records_by_group_id(group_id: str):
    """Get Record document by related group_id identity
    :param group_id identity of related Group with Record"""
    actions = ActionModel.objects(group_id=group_id)
    actions_ids = [action.id for action in actions]
    record = RecordModel.objects(action_id__in=actions_ids)
    if record is None:
        return __not_found_response
    return loads(record.to_json()), 200


def get_records_by_action_id(action_id: str):
    """Get Record document by related action_id identity
    :param action_id identity of related Action with Record"""
    record = RecordModel.objects.get(action_id=action_id)
    if record is None:
        return __not_found_response
    return loads(record.to_json()), 200


def create_record(user):
    """Create new Record document"""
    user_model = UserModel.objects.get(login=user)
    action = ActionModel.objects.get(id=request.json['action_id'])
    seconds = request.json['seconds']
    if 'comment' in request.json:
        comment = request.json['comment']
        created_record = RecordModel(user=user_model, action_id=action, seconds=seconds,
                                     comment=comment).save()
    else:
        created_record = RecordModel(user=user_model, action_id=action, seconds=seconds).save()
    return {'id': str(created_record.id)}, 201


def remove_record_by_id(record_id: str):
    """Delete the existed group_id
    :param record_id -- Identity of the Record document to remove"""
    RecordModel.objects.get(id=record_id).delete()
    return NoContent, 204
