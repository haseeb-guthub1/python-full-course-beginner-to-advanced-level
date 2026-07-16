a = int(input("enter a no: "))
b = int(input("enter a no: "))

if( a == 0 or b == 0 ):
    raise ZeroDivisionError("hey ypur program is not meant to divide  numbers by zero")

else:
    print(f" the division of a/b is: {a/b}")