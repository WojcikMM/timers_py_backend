from datetime import datetime
from mongoengine import BooleanField
from mongoengine import CASCADE
from mongoengine import Document, StringField, DateTimeField, EmailField
from mongoengine import ReferenceField, DecimalField

avalible_roles: [str] = ['User', 'Admin']


class User(Document):
    login = StringField(min_length=4, required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(min_length=5, max_length=50, required=True)
    role = StringField(choices=avalible_roles, default='User')
    created_at = DateTimeField(default=datetime.utcnow)


class GroupModel(Document):
    name = StringField(required=True, unique=True)
    active = BooleanField(required=True, default=True)
    created_at = DateTimeField(default=datetime.utcnow)


class ActionModel(Document):
    group_id = ReferenceField(GroupModel, reverse_delete_rule=CASCADE, required=True)
    name = StringField(required=True, min_length=5)
    active = BooleanField(required=True, default=True)
    created_at = DateTimeField(default=datetime.utcnow)


class Record(Document):
    action_id = ReferenceField(ActionModel, required=True)
    seconds = DecimalField(precision=0, required=True)
    comment = StringField()
    user = ReferenceField(User, required=True)
    created_at = DateTimeField(default=datetime.utcnow)
