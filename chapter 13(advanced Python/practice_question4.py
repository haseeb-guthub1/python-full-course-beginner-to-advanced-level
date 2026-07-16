# find the maximuim number using the reduce function?

from functools import reduce

l = [1,2,3,4,5,6,12,7,8,99]

def number(a,b):
    if(a>b):
        return a
    return b

print(reduce(number,l))