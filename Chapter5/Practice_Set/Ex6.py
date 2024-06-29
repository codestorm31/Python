'''
6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.
'''

d={}

for i in range(0,4):
    name=input("Enter Name:")
    lang=input("Enter favourite Language:")
    d[name]=lang
    
print(d)