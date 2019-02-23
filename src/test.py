from mongoengine import connect

from modules.database.models.action import Action
from modules.database.models.group import Group

connect('mongoengine_test', host='localhost', port=27017)
group = Group(name='Test2')
group.save()





action = Action(name='ActionTest2', group=group)
action.save()

print(Action.objects().to_json())