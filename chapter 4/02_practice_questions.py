# 1: write a program to store a 7 fruits name in a list entered by a users?

fruits = []
f1= input("enter a fruit name: ")
fruits.append(f1)
f2= input("enter a fruit name: ")
fruits.append(f2)
f3= input("enter a fruit name: ")
fruits.append(f3)
f4= input("enter a fruit name: ")
fruits.append(f4)
f5= input("enter a fruit name: ")
fruits.append(f5)
f6= input("enter a fruit name: ")
fruits.append(f6)
f7= input("enter a fruit name: ")
fruits.append(f7)

print(fruits)


# 2:  write a program to accept marks of 6 students and display them in a sorted manner?

Marks= []
f1= int(input("enter a marks: "))
Marks.append(f1)
f2= int(input("enter a marks: "))
Marks.append(f2)
f3= int(input("enter a mar: "))
Marks.append(f3)
f4= int(input("enter a marks: "))
Marks.append(f4)
f5= int(input("enter a marks: "))
Marks.append(f5)
f6= int(input("enter a marks: "))
Marks.append(f6)
f7= int(input("enter a makrks: "))
Marks.append(f7)

print(Marks)
c = Marks.sort()
print(Marks)


# 4:check that a tuple cannot change in python?

a = ("Haseeb", 3.13 ,1, 2.12 )
#  cannot change in tuple
a[0]= "hassan" 

# write a program to count the no of zero in a tuple?
a =(7,0,8,0,0,9)

print(a.count(0))


# 5: write a program to sum a list with 4 number?

l = (1,3,2,4)
print(sum(l))



