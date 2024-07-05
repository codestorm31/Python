# 1. Write a program using functions to find greatest of three numbers.

def goat(l):
    print(max(l))

l=[None]*3
for i in range(0,3):
    l[i]=int(input())
    
goat(l)