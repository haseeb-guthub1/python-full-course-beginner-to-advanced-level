class employee  :
    language = "py" #this is  a class attribute
    salary = 1200000

    def __init__(self,name, salary, language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

    def getInfo(self):
        print(f"the language is {self.language}, The sallary is {self.salary}")



    @staticmethod
    def greet():
        print("good morning")    


haseeb = employee("Haseeb",130000, "javascript")

print(haseeb.name, haseeb.salary, haseeb.language)

