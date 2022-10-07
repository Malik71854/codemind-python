n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i==0:
        l1.append(i)
    if i==1:
        l2.append(i)
print(*l1+l2)