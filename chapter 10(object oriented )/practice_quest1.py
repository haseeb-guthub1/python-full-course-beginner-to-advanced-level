# create a class programmerfor sorting information of few programmers wprking at microsoft?

class programmer:
    company = "microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode


p = programmer("Haseeb",120000,24000)
print(p.name, p.salary ,p.pincode , p.company)

r= programmer("hassan",130000,240120)
print(r.name, r.salary ,r.pincode , r.company)

        