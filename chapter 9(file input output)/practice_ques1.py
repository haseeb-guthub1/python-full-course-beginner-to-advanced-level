# write the program to read the text from "poems.txt " file and find whether it contains the words twinkle?``

# f = open("poems.txt","r")
# print(f.read())
# f.close()


with open("poems.txt") as f:
    data = f.read()
    poem = data.find("twinkle")
   

    print( poem)

