#2. Write a program to accept marks of 6 students and display them in a sorted manner.

l1=[]

for i in range(1,7):
    temp=int(input("Enter Marks:"))
    l1.append(temp)

l1.sort()
print(l1)