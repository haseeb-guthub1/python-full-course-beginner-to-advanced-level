"""
factorial
5!=5*4*3*2*1

"""
n = int(input("enter no: ")) 
def factorial(n):
    if (n==1 or n==0):
        return 1
    
    return n *factorial(n-1)  

print(f"the factorial is: , {factorial(n)}") 
