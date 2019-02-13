from src.modules.database.main.main_db import MainDatabase


class ActionsCollectionProvider(MainDatabase):
    """Provider to handling database objects of Actions documents"""

    def __init__(self):
        """
            Generate new instance of Action database provider
        """
        super().__init__('actions')
