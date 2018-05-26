'''
examples of functions which replaces spaces more than 2 with one space, two only on the end or the start of string, 
last one replace also between spaces
'''
import re

def clean(string):
    '''
    function which cleans string from empty spaces on the start and on the end of string for example:
    input is : "   Hello World    " and output is "Hello World"
    '''
    first = 0
    for item in string:
        if item != ' ':
            first = string.index(item)
            break
    string = string[::-1]
    last = 0
    for item in string:
        if item != ' ':
            last = string.index(item)
            break
    return string[::-1][first:len(string)-last]
    
def clean2(string):
    '''
    function which cleans string from empty spaces on the start and on the end of string for example:
    input is : "   Hello World    " and output is "Hello World"
    '''
    nonempty = [string.index(item) for item in string if item != ' ']
    nonempty2 = [string[::-1].index(item) for item in string[::-1] if item != ' ']
    return string[nonempty[0]:len(string) -nonempty2[0]]

def clean3(string):
    '''
    this function is using regex to clean string from rebundant spaces
    '''
    try:
        for item in re.findall('[" "]{2,}',string):
            string = string.replace(item, ' ')
            if string[0] == ' ':
                string = string[1:]
            if string[-1] == ' ':
                string = string[:-1]
        return string
    except:
        return string
