n =int(input())
p =abs(n)
s =str(p)
s1 =s[::-1]
a =int(s1)
if n<0:
    print("-{}".format(a))
else:
    print(a)