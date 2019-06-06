a1,b1=input().split()
a1=int(a1)
b1=int(b1)
for x in range(a1+1,b1):
    if x%2==0:
        print(x,end=' ')
