'''
6. Write a program to calculate the grade of a student from his marks from the
following scheme:
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50 => F
'''

mark=int(input("Enter mark:"))

if(mark<50):
    print("F")
elif(mark>=50 and mark<60):
    print("E")
elif(mark>=60 and mark<70):
    print("D")
elif(mark>=70 and mark<80):
    print("C")
elif(mark>=80 and mark<90):
    print("B")
else:
    print("A")