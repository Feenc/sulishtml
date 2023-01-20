import random

minimumErtek=int(input("Add meg hogy hol kezdődjön: "))
maximumErtek=int(input("Add meg hogy hol végződjön: "))
darab=int(input("Hány darab kell: "))

lista=[]

for i in range(darab):
    lista.append(random.randint(minimumErtek, maximumErtek))

print(lista)

legnagyobb=max(lista)
egyseg=80//legnagyobb

for e in lista:

    print(e)
