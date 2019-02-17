from abc import ABCMeta, abstractmethod


class MainDatabaseProviderAbstract(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, collection_name: str):
        """ Create an instance of Main DataBase Connection"""
        pass

    @abstractmethod
    def insert_document(self, document: {}) -> str:
        """Inserting new document into collection
        :param document: instance of document to insert into collection
        :return new identity of created document
        """
        pass

    @abstractmethod
    def get_all_documents(self) -> iter:
        """Get all documents in collection as Database_Cursor
        """
        pass

    @abstractmethod
    def get_document_by_id(self, document_id: str) -> {}:
        """Returns first element in database with target id, if exists
        :param document_id - identity of document in target collection
        """
        pass

    @abstractmethod
    def get_document_by_filter(self, **kwargs):
        pass

    @abstractmethod
    def delete_document_by_id(self, document_id: str) -> str:
        """
        Remove target document from collection
        :param document_id - identity of document in target collection to delete
        :rtype: returns deleted identity or None if not exists
        """
        pass

    @abstractmethod
    def update_document_by_id(self, document_id: str, updated_properties: {}) -> str:
        """Update document with specific identity  and return it identity if exists.
        Else return None value.
        :param document_id: Document identity value
        :param updated_properties: A dictionary with key:value properties to update
        :return: target document identity if exists else returns None
        """
        pass

    @abstractmethod
    def any_documents(self, **kwargs) -> bool:
        """
            Search collection for documents with specyfied arguments
            If any exists returns True else return False
        """
        pass

    @abstractmethod
    def __del__(self):
        """Method fired when object is removed from memory"""
        pass
