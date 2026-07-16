# to filter a list of no divisible by 5

l = [1,2,3,4,5,10,15,8]

def divisible(n):

    if (n%5 == 0):
        return True
    
    return False
a = filter(divisible,l)
print(list(a))