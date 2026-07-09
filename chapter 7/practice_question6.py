# calculate the factorial of a given no using for loop?
# 5! = 1*2*3*4*5
n = int(input("enter a no: "))
prod = 1
for i in range(1, n+1):
    prod = prod*i
print(f"the factorial of {n} is {prod} ")


