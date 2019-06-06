a1,b1=input().split()
g=[]
j=''
for x in range(int(a1)+1,int(b1)):
    d=0
    e=x
    while (e!=0):
        c=int(e%10)
        f=int(e/10)
        d=d+(c*c*c)
        e=f
    if (d==x):
        g.append(x)
for i in range(len(g)-1):
    j+=str(g[i])+" "
print(j+str(g[-1]))
