n=int(input())
l=list(map(int,input().split()))
s=""
for i in l:
    s=s+str(i)
z=int(s)+1
zz=str(z)
for i in zz:
    print(i,end=" ")