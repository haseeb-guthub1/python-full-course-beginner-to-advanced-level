# write a program to create a dictionary of hindu words with value as their eng translator?
words = {
    "madad" : "help",
    "khursi": "chair",
    "beli" : "cat"

}
word = input( "enter a words you means of : " ) 
print(words[word])



# write a program to enter a 8  no from user and display all the unique   numbers ones

s = set()
no1 = int(input("enter no1: "))
s.add(no1)
no2 = int(input("enter no2: "))
s.add(no2)
no3 = int(input("enter no3: "))
s.add(no3)
no4 = int(input("enter no4: "))
s.add(no4)
no5 = int(input("enter no5: "))
s.add(no5)
no6 = int(input("enter no6: "))
s.add(no6)
no7 = int(input("enter no7: "))
s.add(no7)
no8 = int(input("enter no8: "))
s.add(no8)

print(s)


# can we have a set with 18(int)  and 18(str) as a value in it?

s = set()
s.add(18)
s.add("18")

print (s)


# create an empty dict aallow 4 four friends to add their favourite  language as value and use their key  as their name?
d = {}
name = input("enter name: ")
language = input("enter favourite language: ")
d.update({name : language})

name = input("enter name: ")
language = input("enter favourite language: ")
d.update({name : language})

name = input("enter name: ")
language = input("enter favourite language: ")
d.update({name : language})

name = input("enter name: ")
language = input("enter favourite language: ")
d.update({name : language})
print(d)


# can yu change the values inside a list which is contain on a set?

s={8, 7, 12, "haseeb", [1,2]}
# no change occur because we cannot add list in set
