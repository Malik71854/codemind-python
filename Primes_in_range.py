from math import *
def isprime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return False
        return True
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if isprime(i):
        c+=1
print(c)