class employee:
    company = "ITC"
    name = "default"
    def show(self):
        print(f"the name is {self.name} and the company  is {self.company}")


class coder:
    language = "python" 
    
    def printlanguage(self):
        print(f" out off all . here is your language {self.language}")


class programmer(employee, coder):
    company = "SYSTEM"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good in  {self.language} language")


a = employee()
b = programmer()

b.show()
b.printlanguage()
b.showlanguage()





