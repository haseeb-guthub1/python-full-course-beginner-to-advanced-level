# 1:write a python program to display a user entered name followed by good afternoon using input() function.

name = input("please enter a name: ")
print("Good Afternoon", name)

# 2: write a program to fill in the letter templates given below with name and date. Use input() function to take name and date from user.

letter = """Dear <|name|>,
you are selected!
<|date|>"""
print(letter.replace("<|name|>", input("enter your name: ")).replace("<|date|>", input("enter the date: ")))



# 3:write a program to detect doule space in a string ?


str = "Haseeb is a good person and he is a    good student"
print(str.find("  "))  # prints the index of the first occurrence of double space

# 4: replace the double space with a single space as we do in problem 3?

str = "Haseeb is a good person and he is a    good student"
print(str.replace("  ", " "))  # replaces double space with single space and prints the new string


# 5: write a program to format the letter using escape sequence characters. Use the following letter template.

letter = "Dear Haseeb,\nthis python course is nice.\nThanks!"
print(letter)  # prints the letter with new lines using escape sequence characters