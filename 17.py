e=int(input())
c=0
a=e
while a>0:
    b=e%10
    c=c+(b*b*b)
    d=int(a/10)
    a=d
if (c==e):
    print("yes")
else:
    print("no")
