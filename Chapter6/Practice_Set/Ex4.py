'''4. Write a program to find whether a given username contains less than 10
characters or not.'''

str=input("Enter username:")

if(len(str)<10):
    print("Too short")
else:
    print("Valid username")
