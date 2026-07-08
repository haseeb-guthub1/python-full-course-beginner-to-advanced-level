# write a program to find the greatest of four no entered by the users?

no1 = int(input("enter a number: "))
no2 = int(input("enter a number: "))
no3 = int(input("enter a number: "))
no4 = int(input("enter a number: "))

if(no1>no2 and no1>no3 and no1>no4):
    print("no1 is greater no:", no1)

elif(no2>no1 and no2>no3 and no2>no4):
    print("no2 is greater no: ", no2)

elif(no3>no1 and no3>no2 and no3>no4):
    print("no3 is greater no: ",no3)  

elif(no4>no1 and no4>no2 and no4>no3):
    print("no4 is greater no :",no4)  

else:
    print("enter no is not greater")

# write a program to check whether a student is pass or fail they contain total 40% marks and each subj 33% take the marks from user?

no1 = int(input("enter a number: "))
no2 = int(input("enter a number: "))
no3 = int(input("enter a number: "))
per1= (no1/100)*100
per2= (no3/100)*100
per3= (no3/100)*100

if (per1>=33 and per2>=33 and per3>=33):
    print("student is passed",)
else:
    print("student is failed")   

total_percentage = ((no1 + no2 + no3)/300)*300

if (total_percentage>=40):
    print(" student is passed", total_percentage)

else:
    print("student is failed", total_percentage)


# spam comment is defined as a text containing following keywords?

p1 =    "make alot of money"
p2 =  "buy now"
p3 = "subscribe this"
p4 = "click this"

msg =  input("enter a msg: ")
if(p1 in msg or p2 in msg or p3 in msg or p4 in msg ):
    print ("its a scam msg ")
else:
    print("this msg is not a scam")    



# write a program to find whether a username contains less then 10 character or not?

username = input("enter a name: ")

if(len(username)<10):
    print("contain less then character:")

else:
    print("greater then the length ")    


# write a program to find to out a given name is present on a list or not? 
l = ["haseeb", "hassan", "aqib"]
name = input("enter a name: ")
if(name in l):
    print("present in a list")
else:
    print("not in the list")    


# write a program to find out whether the given post is talking about haseeb or not?
post = "hey i am haseeb and haseen is a good developer"
if("haseeb" in post):
    print("haseeb is in post")
else:
    print("haseeb is not in post")    

