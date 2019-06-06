a1=int(input())
fact=1
if(a1>0):
    for i in range(1,a1+1):
        fact=fact*i
    print(fact)
elif(a1==0):
    fact=1
    print(fact)
else:
    print("invalid")

