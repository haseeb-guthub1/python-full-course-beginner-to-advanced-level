def goodday(name, ending):
    print("good day,"+ name)
    print(ending)

goodday("haseeb", "thankuyou")   
goodday("hassan", "thankuyou")   
goodday("aqib", "thankuyou")   



# return function
def goodday(name, ending):
    print("good day,"+ name)
    print(ending)
    return "done"

a = goodday("haseeb", "thankyou")
print(a)