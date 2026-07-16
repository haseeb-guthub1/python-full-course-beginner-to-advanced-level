# list comprehension  to print a list which contain the multiplication table of a user entered number?


n = int(input("enter a no: "))

table = [n*i for i in range(1,11)]
print(table)
