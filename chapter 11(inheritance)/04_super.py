class emplyee:
    def __init__(self):
        print("constructor of employee")
    a = 1


class programmer(emplyee):
    def __init__(self):
        print("constructor of programmer")
    b = 2


class manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c= 3

# o =emplyee()
# print(o.a)    


# o  = programmer()
# print(o.b)


o = manager()
print(o.a, o.b, o.c )
