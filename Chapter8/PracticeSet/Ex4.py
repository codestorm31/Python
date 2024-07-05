# 4. Write a recursive function to calculate the sum of first n natural numbers

def firstN(n):
    sum=0
    if(n==0):
        return 0
    sum= n+firstN(n-1)
    return sum

n=int(input())
print(firstN(n))