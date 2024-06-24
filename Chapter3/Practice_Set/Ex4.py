#4. Replace the double space from problem 3 with single spaces.

str=input("Enter any string:")

ind=str.find("  ")

if(ind==-1):
    print("Double Space not found")
else:
    print(str.replace("  "," "))