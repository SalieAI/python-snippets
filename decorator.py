'''
Example of using decorator ...
'''

def milk(func):
    def wrapper(*arg):
        res = func(*arg)
        return res + 1.2
    return wrapper

def coffee(func):
    def wrapper(*arg):
        res = func(*arg)
        return res + 2.0
    return wrapper

@milk
@coffee
def bill():
    return 0
