with open("this.txt") as f:
    data=f.read()

with open("this_copy.txt") as f:
    context = f.read()

if(data == context):
    print("the data is matched")
else:
    print("the data is not matched")
