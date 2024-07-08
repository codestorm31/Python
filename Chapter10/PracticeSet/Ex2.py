'''
2. Write a class “Calculator” capable of finding square, cube and square root of a
number.
'''

class Calculator:
    def __init__(self,n):
        self.n=n
        sq=pow(n,2)
        sqrt=pow(n,1/2)
        cube=pow(n,3)
        print(f"{sq} & {sqrt} & {cube}")
        
c1=Calculator(4)
