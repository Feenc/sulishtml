def oszlopba(munkalista, db):
    for i in range(len(munkalista)):
        print(munkalista[i],end=" ")
        if i%db==db-1:
            print()
print()    



lista=[]
for i in range (10):
    lista.append(int(input("Kérek egy számot: ")))

lista=[1,2,3,4,5,6,7,8,9,0]
print(lista)

for i in range(len(lista)):
    print(lista[i],end=" ")
    if i%3==2:
        print()
print()


szamBe=int(input("Kérek egy számot: "))
if szamBe in lista:
    print("van benne")
else:
    print("nincs benne")

oszlopba(lista,5)    
