# add a statuc method of question  2 and greet the user with hello?

# quetsion 2: class calculator to find the capible of finding square , cube and square root of the number?

class calculator:
    def __init__(self, n):
        self.n  = n
    @ staticmethod
    def greet() :
        print("HELLO!")   

    def square(self):
        print(f"the square is : {self.n*self.n}")    

    def cube(self):
        print(f"the cube is : {self.n*self.n* self.n}")    

    def square_root(self):
        print(f"the square root is : {self.n**1/2}")    



a = calculator(4)
a.greet()
a.square()
a.cube()
a.square_root()