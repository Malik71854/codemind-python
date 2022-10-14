n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s1=set(l1)
s2=set(l2)
l3=list(s1)
l4=list(s2)
l=l3+l4
l5=[]
for i in l:
    c=l.count(i)
    if c==1:
        l5.append(i)
print(len(l5))