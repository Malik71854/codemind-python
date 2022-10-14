n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in range(0,n-1):
    if i!=0 and i!=n-1:
        if l[i-1]%2!=0 and l[i+1]%2!=0 and l[i]%2!=0:
            cnt+=1
print(cnt)