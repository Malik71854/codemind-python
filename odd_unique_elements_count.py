n=int(input())
l=list(map(int,input().split()))
cnt=0
s=set(l)
for i in s:
    if i%2!=0:
        cnt+=1
print(cnt)
        