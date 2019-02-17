"""Controller to handling request where target is record object"""
from connexion import request, NoContent
from injector import inject

from modules.abstracts.database.collection_providers.collection_providers_abstract import \
    RecordsCollectionProviderAbstract


@inject
def get_all_records(provider: RecordsCollectionProviderAbstract) -> None:
    """
    Returns all records from database
    :param provider: Abstract declaration of RecordCollectionProvider
    :return: list of record documents
    """
    return provider.get_all_documents(), 200


@inject
def get_record(record_id: str, provider: RecordsCollectionProviderAbstract) -> None:
    """Get record by record identity
    :param record_id identity of specific record
    :param provider: Abstract declaration of RecordCollectionProvider
    """
    return provider.get_document_by_id(record_id), 200


@inject
def create_record(provider: RecordsCollectionProviderAbstract) -> None:
    """Create new record
    :param provider: Abstract declaration of RecordCollectionProvider
    """
    body = request.json
    print(body)
    return provider.insert_document(body), 201


@inject
def delete_record(record_id: str, provider: RecordsCollectionProviderAbstract) -> None:
    """Delete the existed record
    :param provider: Abstract declaration of RecordCollectionProvider
    :param record_id -- Identity of the record to remove"""
    status_code = 404 if provider.delete_document_by_id(record_id) is None else 204
    return NoContent, status_code
