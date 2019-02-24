from operator import itemgetter
from connexion import request, NoContent

from modules.attributes.authorize import AuthorizeAttribute
from modules.database.models import User, avalible_roles
from modules.security.jwt import generate_token


def login_user() -> {dict, int}:
    """Authorize user and return json object with Bearer Token"""
    login, password = itemgetter('login', 'password')(request.json)
    user = User.objects.get(login=login, password=password)
    return {'token': generate_token(user)}, 200


def register_user():
    User(**request.json).save()
    return {'token': generate_token(request.json)}, 200


@AuthorizeAttribute(['User', 'Admin'])
def update_user_properties(user_id: str,token_info):
    email, password = itemgetter('email', 'password')(request.json)
    user = User.objects.get(login=user_id)
    if email is not None:
        user.password = email
    if password is not None:
        user.password = password
    user.save()
    return NoContent, 200


@AuthorizeAttribute(['Admin'])
def update_user_role(token_info):
    user_login, new_role = itemgetter('user_login', 'new_role')(request.json)
    if new_role not in avalible_roles:
        return {'message': 'This role is forbidden!'}, 403
    user = User.objects.get(login=user_login)
    if user is None:
        return {'message': 'User with this login not exists!'}, 404
    user.role = new_role
    user.save()
    return {'message': 'Role successfully updated.'}, 200
