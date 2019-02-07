from src.modules.database.main.main_db import MainDatabase


class GroupsCollection:
    def __init__(self, main_connection: MainDatabase):
        self.__main_connection = main_connection
        self.__collection_name = 'groups'

    def get_all_groups(self)-> []:
        """
        Returns array of all documents from collection
        :return: array of documents
        """
        return [doc for doc in self.__main_connection.get_all_documents(self.__collection_name)]

    def get_group_by_id(self, group_id: str) -> {}:
        """
        Get specific document from collection by identity
        :param group_id: current document identity
        :return: found document from collection
        """
        return self.__main_connection.get_document_by_id(self.__collection_name, group_id)

    def create_group(self, group_object: {}) -> str:
        """
        Create new group document in groups collection
        :param group_object: document with specific properties
        :return: identity from created document
        """
        return self.__main_connection.insert_document(self.__collection_name, group_object)

    def update_group(self, group_id: str, update_group_properties: {})-> str:
        """
        Update properties in group with specified identity
        :param group_id: identity of target document to update
        :param update_group_properties:  properties witch may be updated
        :return: updated group identity if specific group exists
        """
        return self.__main_connection.update_document_by_id(group_id, update_group_properties)

    def delete_group(self, group_id)-> str:
        """
        Remove group from collection witch have specific identity if exists.
        Else returns None value
        :param group_id: identity of group to remove
        :return: Identity of removed document if exists. Else return None
        """
        return self.__main_connection.delete_document_by_id(group_id)
