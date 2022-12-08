#1.Kérj be 10 szamot
szamok=[]
#for i in range(10):
#    szamok.append(int(input(str(i+1)+". szám: ")))
szamok=[1,2,3,4,5,6,7,8,9,0]
#2.feladat: a szamokat irasd ki egymas melle

for i in szamok:
    print(str(i),end="")
print()
print("vége")
#3.irasd ki 2 oszlopba
for i in range(10):
    print(str(szamok[i])+"\t",end="")
    if i%3==2:
        print()

print()

#4.Szamold ossze a szamok osszeget
átlag=sum(szamok)/len(szamok)
print(átlag)

osszeg=0
for i in szamok:
    osszeg+1
    #osszeg=osszeg+1
átlag=osszeg/len(szamok)
print(átlag)
#5.feladat tarold el a szoveget
szoveg="aújioaúpspijiújgúajpoeeeeeeekkőkőoalpőú ,aőlfgakgo őkk kopakpkf,fl ofafasfk, oa"
#6.feladat nagybeture csereles
#7.Ismeteld az elozot ures sor vegjelig
betu="qwe"
while betu!="":
    betu=input("Kérek egy betut: ")
    szoveg=szoveg.replace(betu,betu.upper())

    print(szoveg)

#8.feladat irasd ki a szoveget forditva
lista=szoveg.split(" ")
lista.reverse
szoveg2=" ".join(lista)
print(szoveg2)
#9.feladat: irasjel torles
jelek=",!?-:;."

szoveg=szoveg.replace(".","")



