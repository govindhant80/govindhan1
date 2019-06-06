a1,b1=input().split()
e=[]
f=''
for i in range(int(a1)+1,int(b1)):
  c=1
  d=0
  while c<=i:
    if i%c==0:
      d+=1
    c+=1
  if d==2:
    e.append(i)
for i in range(len(e)-1):
  f+=str(e[i])+" "
print(f+str(e[-1]))
