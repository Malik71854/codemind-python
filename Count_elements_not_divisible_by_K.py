n,k=map(int,input().split())
l=list(map(int,input().split()))
cnt=0
for i in l:
    if i%k!=0:
        cnt+=1
print(cnt)