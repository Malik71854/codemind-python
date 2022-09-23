n=int(input())
l=list(map(int,input().split()))
s=set(l)
cnt=0
for i in s:
    if i%2==0:
        cnt+=1
print(cnt)
        