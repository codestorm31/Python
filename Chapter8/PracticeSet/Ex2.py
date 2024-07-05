# 2. Write a python program using function to convert Celsius to Fahrenheit

def conv(c):
    f=c*9/5  + 32
    return f

c=int(input())
print(conv(c))