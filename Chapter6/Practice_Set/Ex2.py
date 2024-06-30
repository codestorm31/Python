'''2. Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.'''


a=int(input("Enter marks:"))    
b=int(input("Enter marks:"))    
c=int(input("Enter marks:"))    

avg=(a+b+c)/3

if(avg>=40  or (a>=33 and b>=33 and c>=33)):
    print("Pass")
    
else:
    print("Fail")