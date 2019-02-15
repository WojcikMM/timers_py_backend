from modules.database.main.main_database_provider import MainDatabaseProvider


class UsersCollectionProvider(MainDatabaseProvider):
    """Provider to handling database objects of Actions documents"""

    def __init__(self):
        super().__init__('users')
