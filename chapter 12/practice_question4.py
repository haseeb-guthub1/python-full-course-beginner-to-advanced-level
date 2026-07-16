# display a/b where a and b are integers if b=0 display infinite by handling the zerodivisionerror?

a = int(input("enter value a: "))
b = int(input("enter value b: "))

if( b == 0 ):
    raise ZeroDivisionError("hey your program is not meant to divide  numbers by zero")

else: 
    print(f"the division if a/b is {a}")
