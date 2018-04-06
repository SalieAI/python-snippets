'''
small simple snippet to use threading module for paralel running of some function
'''
import time
from threading import Thread


def no_arg(func, instances):
    
    '''
    no_arg will start function func which is function without arguments on threads where number of threads equals instances
    '''
    
    for i in range(instances):
        t = Thread(target=func)
        t.start()

def with_arg(func, instances,args):
    
    '''
    with_arg will start function func which is function with arguments on threads where number of threads 
    equals instances and with arguments in tuple
    '''
    
    for i in range(instances):
        t = Thread(target=func, args = args)
        t.start()
