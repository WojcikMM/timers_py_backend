from bson.objectid import ObjectId
from pymongo import MongoClient


class MainDatabase:
    def __init__(self, connection_string: str, database_name: str):
        """ Create an instance of Main DataBase Connection
        :param connection_string - connection_string to Database
        :param database_name - name of using database
        """
        self.__database_name = database_name
        self.__client = MongoClient(connection_string)
        self.__database = self.__client.get_database(database_name)

    def insert_document(self, collection_name: str, document: {}) -> str:
        """Inserting new document into collection
        :param document: instance of document to insert into collection
        :param collection_name - name of collection to use
        :return new identity of created document
        """
        collection = self.__database.get_collection(collection_name)
        new_id = collection.insert_one(document).inserted_id
        return str(new_id)

    def get_all_documents(self, collection_name: str) -> iter:
        """Get all documents in collection as Database_Cursor
        :param collection_name - name of collection to use
        """
        collection = self.__database.get_collection(collection_name)
        return collection.find()

    def get_document_by_id(self, collection_name: str, document_id: str) -> {}:
        """Returns first element in database with target id, if exists
        :param collection_name: name of collection to use
        :param document_id - identity of document in target collection
        """
        collection = self.__database.get_collection(collection_name)
        return collection.find_one({'_id': ObjectId(document_id)})

    def delete_document_by_id(self, collection_name: str, document_id: str) -> str:
        """
        Remove target document from collection
        :param collection_name: name of collection to use
        :param document_id - identity of document in target collection to delete
        :rtype: returns deleted identity or None if not exists
        """
        collection = self.__database.get_collection(collection_name)
        deleted_document = collection.find_one_and_delete({'_id': ObjectId(document_id)})
        return deleted_document['_id'] if '_id' in deleted_document else None

    def update_document_by_id(self, collection_name: str, document_id: str, updated_properties:{}) -> str:
        """Update document with specific identity  and return it identity if exists.
        Else return None value.
        :param collection_name: name of collection to use
        :param document_id: Document identity value
        :param updated_properties: A dictionary with key:value properties to update
        :return: target document identity if exists else returns None
        """
        collection = self.__database.get_collection(collection_name)
        updated_document = collection.update_one({'_id': ObjectId(document_id)}, updated_properties)
        return updated_document['_id'] if '_id' in updated_document else None

    def __del__(self):
        """Method fired when object is removed from memory"""
        self.__client.close()
        print('Connection closed.')
