from mongoengine import Document

from modules.errors.database_errors import BadDocumentTypeError


class MainDatabaseProvider:
    def __init__(self, model: type):
        self.model = model

    def insert_document(self, document) -> Document:
            return document.save()

    def get_all_documents(self, **kwargs)-> [Document]:
        return self.model.objects(kwargs)

    def find_one_document(self, **kwargs)->Document:
        return self.model.objects.get(kwargs)

    def remove_document(self, document_id):
        document = self.model.objects.get(id=document_id)
        document.delete()

    def update_document(self, document_id, document:Document):
        if isinstance(type(self.model), document):
            find_document:Document = self.model.objects.get(id=document_id)
            find_document.update(document)
            return find_document.save()
        else:
            raise BadDocumentTypeError(self.model)



