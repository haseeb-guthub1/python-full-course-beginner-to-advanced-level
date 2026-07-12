with open("poems.txt") as f:
   data =  f.read()


with open("poem.txt","w") as f:
   f.write(data) 