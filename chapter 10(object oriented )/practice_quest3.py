# create a class with class attrubute  a , create an ibject from
#  it and set a directly using object.a= 0 
# does it change the class attribute?

class demo :
    a  = 4

o = demo()
print(o.a)#print the class attribute  because instance attribute in not present
o.a = 0  # instance attribute is set
print(o.a)# print the instance  attribute  because instance attribute in  present
print(demo.a) # print class attribute 