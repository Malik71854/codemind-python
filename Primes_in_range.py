import math
def prime(n):
    if n==1:
        return False
    else:
        e =int(math.sqrt(n))
        for j in range(2,e+1):
            if n%j==0:
                return False
        return True
            
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if(prime(i)):
        c+=1
print(c)
    