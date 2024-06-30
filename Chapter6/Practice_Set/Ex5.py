# 5. Write a program which finds out whether a given name is present in a list or not.

l=["Aryan","Ravi","Virat","Rohit"]

name1="Ravi"
name2="Aiden"

if name1 in l:
    print("Found ",name1)
elif name2 in l:
    print("Found ",name2)
else:
    print("Not Found")