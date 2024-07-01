#1. Write a program to print multiplication table of a given number using for loop.

a=int(input("Enter Number:"))
for i in range(1,11):
    print(f"{a}x{i}={a*i}")