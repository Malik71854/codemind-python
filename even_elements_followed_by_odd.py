n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    if i%2!=0:
        l2.append(i)
L=l1+l2
print(*L)