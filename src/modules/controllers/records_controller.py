"""Controller to handling request where target is record object"""
from json import loads
from connexion import request, NoContent
from modules.database.models import RecordModel

__not_found_response = {'messaage': 'No Records found'}, 404


def get_all_records():
    """Returns all Records from database"""
    return loads(RecordModel.objects().to_json()), 200


def get_record_by_id(record_id: str):
    """Get Record document by record_id identity
    :param record_id identity of specific Record"""
    record = RecordModel.objects.get(id=record_id)
    if record is None:
        return __not_found_response
    return loads(record.to_json()), 200


# test it
def get_records_by_group_id(group_id: str):
    """Get Record document by related group_id identity
    :param group_id identity of related Group with Record"""
    record = RecordModel.objects.get(action_id__group=group_id)
    if record is None:
        return __not_found_response
    return loads(record.to_json()), 200


# test it
def get_records_by_action_id(action_id: str):
    """Get Record document by related action_id identity
    :param action_id identity of related Action with Record"""
    record = RecordModel.objects.get(action=action_id)
    if record is None:
        return __not_found_response
    return loads(record.to_json()), 200


def create_record():
    """Create new Record document"""
    return {'id': RecordModel(**request.json).save().id}, 201


def remove_record_by_id(record_id: str):
    """Delete the existed group_id
    :param record_id -- Identity of the Record document to remove"""
    record: RecordModel = RecordModel.objects.get(id=record_id)
    if record is None:
        return __not_found_response
    delete_return = record.delete()
    print(delete_return)
    return NoContent, 204
