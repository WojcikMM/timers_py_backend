class authorize(object):

    def __init__(self, required_role: str):
        self.__required_role = required_role

    def __call__(self, function):
        def wrapped_function(*args):
            print(f'Here make role validation and authorization. User must have any of these roles ({self.__required_role}) to call this controller action')
            function(*args)
        return wrapped_function



@authorize('Testowa rola')
def myFunc(argument_str: str):
    print('Controller action logic')


myFunc('argument funkcji')

#
# @auth_required_roles('test')
# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")


# a_function_requiring_decoration()
