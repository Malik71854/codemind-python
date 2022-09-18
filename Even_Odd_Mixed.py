n=int(input())
s=0
r=n%10
s=s+r
n=n//10
if r%2==0 and s%2==0 and n%2==0:
    print("Even")
elif r%2!=0 and s%2!=0 and n%2!=0:
    print("Odd")
else:
    print("Mixed")