'''
Example of using decorator ...
'''
import time

def lengthandtime(func):
    
    '''
    decorator returning length of wrapped function with time note
    '''
    
    def wrapper(*arg):
        res = func(*arg)
        print (len(res), time.asctime())
        return res
    return wrapper

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
