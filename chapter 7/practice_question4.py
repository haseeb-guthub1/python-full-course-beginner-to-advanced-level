# write a program to find whether a given no is prime or not?

n = int(input("enter a no : "))

for i in range(2,n):
    if(n%i) == 0:
        print("n is not a prime no")
        break

else:
    print("no is prime  ")