from modules.database.main.main_database_provider import MainDatabaseProvider


class ActionsCollectionProvider(MainDatabaseProvider):
    """Provider to handling database objects of Actions documents"""

    def __init__(self):
        """
            Generate new instance of Action database provider
        """
        super().__init__('actions')
