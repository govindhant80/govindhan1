a=int(input())
r1=list(input().split())
b1=0
for i in range(a):
    if(int(r1[i])>0):
        b=sorted(r1)
        b1=1
    else:
        c=reversed(r1)
if(b1==1):
    print(' '.join(b))
else:
    print(' '.join(c))

