# 3. Write a program to detect double space in a string

str=input("Enter any string:")

ind=str.find("  ")

if(ind==-1):
    print("Double Space not found")
else:
    print("Double Space found at:",ind)