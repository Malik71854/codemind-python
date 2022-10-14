n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=l1+l2
l3=[]
for i in l:
    c=l.count(i)
    if c==1:
        l3.append(i)
print(*l3)