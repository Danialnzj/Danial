import random
z=int(input("how many times should we roll the dice?"))
n=0
s=[]
dic1={}
for i in range(z):
    
    a=random.randrange(1,7)
    b=random.randrange(1,7)
    s+=[a+b]
    n+=1

for j in range(2,13):
    c=s.count(j)
    dic1[j]=c
print(dic1)
m=int(input("enter a sumation you want to calculate it's probability:[2:13]"))
p=dic1[m]/z
print(dic1[m])
print(p)

