a,b,k=map(int,input().split())
cnt=0
for i in range(a,b+1):
    if i%k==0:
        cnt+=1
print(cnt)
        