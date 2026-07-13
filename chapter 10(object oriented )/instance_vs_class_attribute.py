class employee  :
    name = "haseeb" #this is  a class attribute
    language = "py" #this is  a class attribute
    salary = 1200000

haseeb = employee()
print(haseeb.language, haseeb.name, haseeb.salary)   


Hassan = employee()
Hassan.name = "Muhammad Hassan" #this is  an instance attribute
Hassan.language = "Javascript" #this is  an instance attribute
print(Hassan.salary, Hassan.language, Hassan.name)
