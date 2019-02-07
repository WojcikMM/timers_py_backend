from src.modules.database.main.main_db import MainDatabase


class RecordCollection:
    def __init__(self, main_connection: MainDatabase):
        self.__main_connection = main_connection
        self.__collection_name = 'records'

    def get_all_records(self)-> []:
        """
        Returns array of all documents from collection
        :return: array of documents
        """
        return [doc for doc in self.__main_connection.get_all_documents(self.__collection_name)]

    def get_record_by_id(self, record_id: str) -> {}:
        """
        Get specific document from collection by identity
        :param record_id: current document identity
        :return: found document from collection
        """
        return self.__main_connection.get_document_by_id(self.__collection_name, record_id)

    def create_record(self, record_object: {}) -> str:
        """
        Create new record document in records collection
        :param record_object: document with specific properties
        :return: identity from created document
        """
        return self.__main_connection.insert_document(self.__collection_name, record_object)

    def update_record(self, record_id: str, update_record_properties: {})-> str:
        """
        Update properties in record with specified identity
        :param record_id: identity of target document to update
        :param update_record_properties:  properties witch may be updated
        :return: updated record identity if specific record exists
        """
        return self.__main_connection.update_document_by_id(record_id, update_record_properties)

    def delete_record(self, record_id)-> str:
        """
        Remove record from collection witch have specific identity if exists.
        Else returns None value
        :param record_id: identity of record to remove
        :return: Identity of removed document if exists. Else return None
        """
        return self.__main_connection.delete_document_by_id(record_id)
