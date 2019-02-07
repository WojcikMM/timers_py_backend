from src.modules.database.main.main_db import MainDatabase


def deserialize_to_action_object(action_db_object) -> {}:
    """
    Convert from database document to serializable object
    :param action_db_object: object from database
    :return:
    """
    if '_id' not in action_db_object:
        return None
    else:
        return {
            'action_id': str(action_db_object['_id']),
            'group_id': action_db_object['groupId'],
            'name': action_db_object['name'],
            'active': action_db_object['active']
        }


class ActionCollection:
    def __init__(self, main_connection: MainDatabase):
        self.__main_connection = main_connection
        self.__collection_name = 'actions'

    def get_all_actions(self) -> []:
        """
        Returns array of all documents from collection
        :return: array of documents
        """
        return [deserialize_to_action_object(doc) for doc in self.__main_connection.get_all_documents(self.__collection_name)]

    def get_action_by_id(self, action_id: str) -> {}:
        """
        Get specific document from collection by identity
        :param action_id: current document identity
        :return: found document from collection
        """
        database_result = self.__main_connection.get_document_by_id(self.__collection_name, action_id)
        return deserialize_to_action_object(database_result)

    def create_action(self, action_object: {}) -> str:
        """
        Create new action document in actions collection
        :param action_object: document with specific properties
        :return: identity from created document
        """
        return self.__main_connection.insert_document(self.__collection_name, action_object)

    def update_action(self, action_id: str, update_action_properties: {}) -> str:
        """
        Update properties in action with specified identity
        :param action_id: identity of target document to update
        :param update_action_properties:  properties witch may be updated
        :return: updated action identity if specific action exists
        """
        return self.__main_connection.update_document_by_id(self.__collection_name, action_id, update_action_properties)

    def delete_action(self, action_id) -> str:
        """
        Remove action from collection witch have specific identity if exists.
        Else returns None value
        :param action_id: identity of action to remove
        :return: Identity of removed document if exists. Else return None
        """
        print(action_id)
        return self.__main_connection.delete_document_by_id(self.__collection_name, action_id)
