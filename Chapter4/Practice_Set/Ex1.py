#1. Write a program to store seven fruits in a list entered by the user.

l1=[]

for i in range(1,8):
    temp=input("Enter fruit:")
    l1.append(temp)
    
print(l1)