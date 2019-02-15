"""Controller to handling request where target is record object"""
from connexion import request, NoContent
from modules.database.providers.records_collection_provider import RecordsCollectionProvider


def get_all_records() -> None:
    """
    Returns all records from database
    :return: list of record documents
    """
    return RecordsCollectionProvider().get_all_documents(), 200


def get_record(record_id: str) -> None:
    """Get record by record identity
    :param record_id identity of specific record
    """
    return RecordsCollectionProvider().get_document_by_id(record_id), 200


def create_record() -> None:
    """Create new record"""
    body = request.json
    print(body)
    return RecordsCollectionProvider().insert_document(body), 201


def update_record(record_id: str) -> None:
    """ Update the existed record
    :param record_id identity of record to update
    """
    body = request.json
    updated_id = RecordsCollectionProvider().update_document_by_id(record_id, body)
    status_code = 404 if updated_id is None else 200
    return NoContent, status_code



def delete_record(record_id: str) -> None:
    """Delete the existed record
    :param record_id -- Identity of the record to remove"""
    status_code = 404 if RecordsCollectionProvider().delete_document_by_id(record_id) is None else 204
    return NoContent, status_code
