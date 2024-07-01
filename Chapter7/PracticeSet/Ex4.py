#4. Write a program to find whether a given number is prime or not

a=int(input("Enter number:"))
c=0
for i in range(1,a):
    if(a%i==0):
        c+=1

if c==1:
    print("Prime")
else:
    print("Not Prime")