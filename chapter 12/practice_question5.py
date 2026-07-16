# store the multiplication table generated in problem 3    in a file name table.txt?
#question no 3: list comprehension  to print a list which contain the multiplication table of a user entered number?


n = int(input("enter a no: "))

table = [n*i for i in range(1,11)]

with open("tables.txt" , "a") as f:
    f.write(str(table) + "\n")

print(table)
