# using resurcive function to calculate the sum of natural no?

n = int(input("enter a no: "))
def natural(n):
    if(n ==0 or n==1):
        return 1

    return natural(n-1) + n
print(natural(n))