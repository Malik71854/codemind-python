n=int(input())
l=list(map(int,input().split()))
x=sum(l)//len(l)
c=0
for i in l:
    if x==i:
        print("True")
        c+=1
        break
    else:
        continue
if c==0:
    print("False")