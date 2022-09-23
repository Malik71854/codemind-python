n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=0
for i in l:
    if i==m:
        print("True")
        c+=1
        break
    else:
        continue
if c==0:
    print("False")