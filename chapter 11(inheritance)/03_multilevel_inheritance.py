class emplyee:
    a = 1


class programmer(emplyee):
    b = 2


class manager(programmer):
    c= 3

o =emplyee()
print(o.a)    


o  = programmer()
print(o.b)


o = manager()
print(o.a, o.b, o.c )
