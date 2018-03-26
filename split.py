'''Short function to divide text (csv or ...) to small files with defined number of lines'''
import os

def splitter(name, parts = 100000):
    # make dir for files
    if not os.path.exists(name.split('.')[0]):
        os.makedirs(name.split('.')[0])
    f = open(name, 'r', errors = 'ignore')
    lines = f.readlines()
    f.close()
    i = 0
    while i < len(lines):
        for item in lines[i:i+parts]:
            f2 = open(name.split('.')[0]+ '/'name.split('.')[0]+ str(parts)+'.txt', 'a+', errors = 'ignore') 
            f2.write(item)
            f2.close()
    i += parts
