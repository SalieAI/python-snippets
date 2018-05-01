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
    nonemty2 = [string.index(item) for item in string[::-1] if item != ' ']
    return string[nonempty[0]:nonempty[0]+1]
