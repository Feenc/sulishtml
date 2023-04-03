lista=[]
f=open("EUcsatlakozas.txt")
for e in f:
    lista.append(e.replace("\n","").split(";"))
print(lista)

print("3.feladat: Az EU tagállamainak száma: {} db.".format(len(lista)))
szam=[]
for i in lista:
    if i[1][:4]=="2007":
        szam.append(i)

print("4.feladat: 2007-ben {} ország csatlakozott.".format(len(szam)))
        

for o in lista:
    if o[1][:4]=="05":
        
print("5.feladat májusban volt csatlakozás")







f.close



