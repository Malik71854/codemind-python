n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
flag=0
for i in l:
    if i<a or i>b:
        print(i,end=' ')
        flag=1
if flag==0:
    print(-1)