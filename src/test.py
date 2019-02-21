from modules.attributes.authorize import Authorize


@Authorize('Testowa rola')
def myFunc(argument_str: str):
    print('Controller action logic')


myFunc('argument funkcji')

#
# @auth_required_roles('test')
# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")


# a_function_requiring_decoration()
# def capital_case(x):
#     return x.capitalize()


# def test_capital_case():
#     assert capital_case('semaphore') == 'Semaphore'
