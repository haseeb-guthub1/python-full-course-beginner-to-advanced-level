    # a file contain a wrod "donkey " yu need to write a program which replace this wrod with"#####"by updating the same files?

with open("file.text") as f:
    data= f.read()
    replace = data.replace("donkey", "#####")
    print(replace)

with open("file.text","w") as f:
    f.write(replace)    

    