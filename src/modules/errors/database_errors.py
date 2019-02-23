
class BadDocumentTypeError(Exception):
    def __init__(self, document):
        """
        Exception when injected wrong type of document.
        :type document: document with required type.
        """
        self.description = f"Bad document type passed, required type {type(document)}"
