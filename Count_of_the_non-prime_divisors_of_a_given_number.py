def prime(j):
    if j<2:
        return False
    for i in range(2,int(j**0.5)+1):
        if j%i==0:
            return False
    return True
n=int(input())
l=[]
cnt=0
for k in range(2,n):
    if n%k==0:
        l.append(k)
for j in l:
    if not prime(j):
        cnt+=1
print(cnt+2)