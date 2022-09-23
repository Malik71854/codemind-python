n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
flag=0
s=0
for i in l:
    if i<a or i>b:
        s+=i
print(s)
        