from src.modules.database.main.main_db import MainDatabase


class UsersCollectionProvider(MainDatabase):
    """Provider to handling database objects of Actions documents"""

    def __init__(self):
        super().__init__('users')
