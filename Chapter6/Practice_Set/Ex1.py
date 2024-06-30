# 1. Write a program to find the greatest of four numbers entered by the user.

a, b, c, d = map(int, input("Enter four numbers separated by spaces: ").split())
print(max(a,b,c,d))