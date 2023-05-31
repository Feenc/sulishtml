asd=[]
f=open("cb.txt")
for e in f:
        asd.append(e.replace("\n",""))
f.close
print(asd)
asd.pop(1)
print("3.feladat: Bejegyzések száma: {} db.".format(len(asd)))

for e in asd:
   if e[3]=="4":
    print("4.feladat: Volt 4 adást inditó sofőr.")
    break
"""
class radio:
    def __init(self,ora,perc,adasDb,nev):
        self.ora=ora
        self.perc=perc
        self.adasDb=adasDb
        self.nev=nev
"""
#6.feladat
def atszamol_percre(ora, perc):
    percek = (ora * 60) + perc
    return percek

ora = 8
perc = 5
eredmeny = atszamol_percre(ora, perc)
print(eredmeny)


#7.feladat



