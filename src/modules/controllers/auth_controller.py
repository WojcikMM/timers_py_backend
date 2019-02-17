from operator import itemgetter
from connexion import request, NoContent
from injector import inject
from werkzeug.exceptions import Unauthorized

from modules.abstracts.database.collection_providers.collection_providers_abstract import \
    UsersCollectionProviderAbstract
from modules.errors.authorization_error import AuthorizationError
from modules.security.jwt import generate_token


@inject
def login_user(provider: UsersCollectionProviderAbstract) -> {dict, int}:
    """Authorize user and return json object with Bearer Token"""
    login, password = itemgetter('login', 'password')(request.json)
    user = provider.get_document_by_filter(login=login, password=password)
    return {'token': generate_token(user)}, 200


@inject
def register_user(provider: UsersCollectionProviderAbstract) -> {dict, int}:
    """Register new user to application"""
    login, password = itemgetter('login', 'password')(request.json)
    if provider.any_documents(login=login):
        raise AuthorizationError(description=f'User with this login: \'{login}\' is already registred.')
    else:
        provider.insert_document(request.json)
        return {'token': generate_token(request.json)}, 200


@inject
def update_user(user_id: int, provider: UsersCollectionProviderAbstract) -> {dict, int}:
    """Update user password or email"""
    updated_id = provider.update_document_by_id(user_id, request.json)
    status_code = 404 if updated_id is None else 200
    return NoContent, status_code
