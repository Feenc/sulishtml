import random
import math 

l=[]
for i in range(10):
    szam= random.random()
    l.append(math.floor(szam*90)+10)

print(l)

l=[]
for i in range(10):
    l.append(random.randint(10,99))

print(l)

print(random.randint(-1000,1000)*3)
l=[]
for i in range(100):
    l.append(random.randint(-1000,1000)*3)

print(l)

print(sum(l))

