#!python3
'''
date: July 2018

Small script to search inside .py files for specific word, 
for example you have lots of scripts in folder and you want look on examples where you used requests
than you simply use get_search() function where path is path to folder which you wants search and search in this case will be "requests"
'''
import os


def get_in(name, string, substring):
    '''
    check if substring is in  file
    '''
    if substring in string:
        return True

def get_py_files(path = ''):
    '''
    returns list of .py files in specified path
    '''
    return [ item for item in os.listdir(path) if '.py' in item]

def get_search(path = '', search = 'whatever'):
    '''
    check folder for search and returns list of files where string is
    '''
    files = get_py_files(path = path)
    result = []
    for item in files:
        itemPath = os.path.join(path, item)
        with open(itemPath, encoding = 'utf8') as f:
            txt = f.read()
        res =  get_in(item, txt, search)
        if res: result.append(item);
    return result
