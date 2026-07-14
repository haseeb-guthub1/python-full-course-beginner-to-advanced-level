class employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

class programmer:
    company = "SYSTEM"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


    def showlanguage(self):
        print(f"the name is {self.name} and he is good in  {self.language} language")

class programmer(employee):
    company = "SYSTEM"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good in  {self.language} language")


a = employee()
b = programmer()

print( b.company)




