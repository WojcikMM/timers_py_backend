from modules.database.main.main_database_provider import MainDatabaseProvider


class GroupsCollectionProvider(MainDatabaseProvider):
    """Provider to handling database objects of Actions documents"""

    def __init__(self):
        super().__init__('groups')
