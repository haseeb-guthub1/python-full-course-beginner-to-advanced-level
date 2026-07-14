"""create a class pet from class animal and then create 
a classs dog from class pet  add a method bark of dog class"""

class animals:
    pass




class pets(animals):
    pass



class dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

d = dog
d.bark()