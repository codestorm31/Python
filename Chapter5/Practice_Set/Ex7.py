'''
7. If the names of 2 friends are same; what will happen to the program in problem 6?
    Solution- It will update the value of the name key

'''
d={}

for i in range(0,4):
    name=input("Enter Name:")
    lang=input("Enter favourite Language:")
    d[name]=lang

print(d)