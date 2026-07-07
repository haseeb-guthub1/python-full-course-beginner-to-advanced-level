

a = (1,45,32,"Rohan", "Haseeb",False,True)
print(type(a))

b= (1,45,32,"Rohan", "Haseeb",False,True)

# # concatination

c =  a+b
print(c)


# repeating values in tuple
d = a*3
print(d)


# check value in the tuple

print("Rohan" in a)

print(len(a))

i=  a.index("Haseeb")
print(i)

a , b, c, d, e, f, g = a
print(a, b, c, d, e, f, g)