from os import environ

from bson.objectid import ObjectId
from pymongo import MongoClient

from modules.utils.mongo_utils import jsonify_mongodb_object


class MainDatabaseProvider:
    def __init__(self, collection_name: str):
        """ Create an instance of Main DataBase Connection"""
        self.__connection_string = environ['MONGO_CONNECTION_STRING']
        self.__database_name = environ['MONGO_DATABASE_NAME']
        self.__client = MongoClient(self.__connection_string)
        self.__database = self.__client.get_database(self.__database_name)
        self.__collection_name = collection_name

    def insert_document(self, document: {}) -> str:
        """Inserting new document into collection
        :param document: instance of document to insert into collection
        :return new identity of created document
        """
        collection = self.__database.get_collection(self.__collection_name)
        new_id = collection.insert_one(document).inserted_id
        return str(new_id)

    def get_all_documents(self) -> iter:
        """Get all documents in collection as Database_Cursor
        """
        collection = self.__database.get_collection(self.__collection_name)
        return [jsonify_mongodb_object(doc) for doc in collection.find()]

    def get_document_by_id(self, document_id: str) -> {}:
        """Returns first element in database with target id, if exists
        :param document_id - identity of document in target collection
        """
        collection = self.__database.get_collection(self.__collection_name)
        document = collection.find_one({'_id': ObjectId(document_id)})
        return jsonify_mongodb_object(document)

    def delete_document_by_id(self, document_id: str) -> str:
        """
        Remove target document from collection
        :param document_id - identity of document in target collection to delete
        :rtype: returns deleted identity or None if not exists
        """
        collection = self.__database.get_collection(self.__collection_name)
        deleted_document = collection.find_one_and_delete({'_id': ObjectId(document_id)})
        return deleted_document['_id'] if '_id' in deleted_document else None

    def update_document_by_id(self, document_id: str, updated_properties: {}) -> str:
        """Update document with specific identity  and return it identity if exists.
        Else return None value.
        :param document_id: Document identity value
        :param updated_properties: A dictionary with key:value properties to update
        :return: target document identity if exists else returns None
        """
        collection = self.__database.get_collection(self.__collection_name)
        updated_document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": updated_properties})
        return updated_document['_id'] if '_id' in updated_document else None

    def __del__(self):
        """Method fired when object is removed from memory"""
        self.__client.close()
        print('Connection closed.')
