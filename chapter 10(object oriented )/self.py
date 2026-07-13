class employee  :
    language = "py" #this is  a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"the language is {self.language}, The sallary is {self.salary}")
    @staticmethod
    def greet():
        print("good morning")    


haseeb = employee()
haseeb.language = "Javascript"
# haseeb.getInfo()
haseeb.greet()

employee.getInfo(haseeb)
# employee.greet(haseeb)
