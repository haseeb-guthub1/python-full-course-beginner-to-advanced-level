# to mine a file log and find out whether  it contains "python"?

with open("file.txt") as f:
    data = f.read()

if ("python " in data ):
        print("yes python is present")
else:
      print("python is not present")            
