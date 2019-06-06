a1,b1=input().split()
c=[]
d=''
for i in range(int(a1)+1,int(b1)):
    if i%2==1:
        c.append(i)
for i in range(len(c)-1):
    d+=str(c[i])+" "
print(d+str(c[-1]))
