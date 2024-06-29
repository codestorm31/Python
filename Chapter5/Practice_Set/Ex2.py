'''
2. Write a program to input eight numbers from the user and display all the unique
numbers (once)
'''

s=set()

for i in range(0,8):
    inp=int(input("Enter numbers:"))
    s.add(inp)
    
print(s)