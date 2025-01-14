import os

def findBytes():
    lst = os.listdir()
    for file in lst:
        
        print(os.stat(file).st_size)

findBytes()