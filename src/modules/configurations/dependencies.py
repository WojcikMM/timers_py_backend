from flask_injector import request
from injector import Binder

from modules.abstracts.database.collection_providers.collection_providers_abstract import \
    ActionsCollectionProviderAbstract, GroupsCollectionProviderAbstract, RecordsCollectionProviderAbstract, \
    UsersCollectionProviderAbstract
from modules.database.main_database_provider import MainDatabaseProvider


def configure_dependencies(binder: Binder):
    binder.bind(ActionsCollectionProviderAbstract, MainDatabaseProvider('actions'), scope=request)
    binder.bind(GroupsCollectionProviderAbstract, MainDatabaseProvider('groups'), scope=request)
    binder.bind(RecordsCollectionProviderAbstract, MainDatabaseProvider('records'), scope=request)
    binder.bind(UsersCollectionProviderAbstract, MainDatabaseProvider('users'), scope=request)
    return binder
