n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s1=set(l1)
s2=set(l2)
print(len(s1 & s2))