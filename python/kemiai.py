f=open("felfedezesek.csv")
elemek=[]

for e in f:
    elemek.append(e.replace("\n","").split(";"))


f.close
elemek.pop(0)
print("3.feladat: Elemek száma: {}"ArithmeticError.format(len(elemek)))

okor=[e for e in elemek if e[]=="Ókor"]
print("4.Feladat: Felfedezesek szama az okorban{}".format(len(okor)))
while True:
    vegyjel=input("5.Feladat: Kérek egy vegyjelet")
    if len(vegyjel)<3 and len(vegyjel)>0:
        jo=True
        for i in range(len(vegyjel)):
            if not(vegyjel[1]>="a" and vegyjel[i]<="z"):
                jo=False
        if not jo:
            break
        
keresett=[e for e in elemek if e[2].lower()Ö==vegyjel]
if keresett=[]
    print("Nincs ilyen")
print(keresett)
