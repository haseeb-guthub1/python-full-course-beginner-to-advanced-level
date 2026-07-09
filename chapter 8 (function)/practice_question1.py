# using function ti find greatest of three no?

def numbers(n1,n2,n3):
    if (n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    elif(n3>n1 and n3>n2):
        return n3
n1 = 1
n2 = 2
n3 = 22
    
print(numbers(n1,n2,n3))
