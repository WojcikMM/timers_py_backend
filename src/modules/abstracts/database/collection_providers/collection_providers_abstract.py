from modules.abstracts.database.main_database_provider_abstract import MainDatabaseProviderAbstract
from abc import ABCMeta, abstractmethod


class ActionsCollectionProviderAbstract(MainDatabaseProviderAbstract, metaclass=ABCMeta):
    """Provider to handling database objects of Actions documents"""

    @abstractmethod
    def __init__(self):
        """Generate new instance of ActionModel database provider"""
        pass


class GroupsCollectionProviderAbstract(MainDatabaseProviderAbstract, metaclass=ABCMeta):
    """Provider to handling database objects of Actions documents"""

    @abstractmethod
    def __init__(self):
        """Generate new instance of ActionModel database provider"""
        pass


class RecordsCollectionProviderAbstract(MainDatabaseProviderAbstract, metaclass=ABCMeta):
    """Provider to handling database objects of Actions documents"""

    @abstractmethod
    def __init__(self):
        """Generate new instance of ActionModel database provider"""
        pass


class UsersCollectionProviderAbstract(MainDatabaseProviderAbstract, metaclass=ABCMeta):
    """Provider to handling database objects of Actions documents"""

    @abstractmethod
    def __init__(self):
        """Generate new instance of ActionModel database provider"""
