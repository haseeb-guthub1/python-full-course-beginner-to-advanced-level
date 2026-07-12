# # write a python program to find out the line no where python is precent?


with open("file.txt") as f:
    found = False

    for lineno, line in enumerate(f, start=1):
        if "python" in line:
            print(f"Python is present on line {lineno}")
            found = True

if not found:
    print("Python is not present")