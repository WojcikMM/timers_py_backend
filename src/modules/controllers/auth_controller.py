from operator import itemgetter
from connexion import request, NoContent

from modules.attributes import AuthorizeAttribute
from modules.database.models import UserModel, avalible_roles
from modules.security import generate_token


def login_user() -> {dict, int}:
    """Authorize user and return json object with Bearer Token"""
    login, password = itemgetter('login', 'password')(request.json)
    user = UserModel.objects.get(login=login, password=password)
    return {'token': generate_token(user)}, 200


def register_user():
    user = UserModel(**request.json).save()
    return {'token': generate_token(user)}, 200


@AuthorizeAttribute(['User','Admin'])
def update_user_properties(user: str,token_info):
    user = UserModel.objects.get(login=user)
    if 'email' is not request.json:
        user.email = request.json['email']
    if 'password' is not request.json:
        user.password = request.json['password']
    user.save()
    return NoContent, 204


@AuthorizeAttribute(['Admin'])
def update_user_role(token_info):
    user_login, new_role = itemgetter('user_login', 'new_role')(request.json)
    if new_role not in avalible_roles:
        return {'message': 'This role is forbidden!'}, 403
    user = UserModel.objects.get(login=user_login)
    if user is None:
        return {'message': 'UserModel with this login not exists!'}, 404
    user.role = new_role
    user.save()
    return {'message': 'Role successfully updated.'}, 200
