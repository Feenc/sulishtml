#1.
szam=[]
for i in range(7):
    szam.append(int(input("Kérek egy számot: ")))
print(szam)
#2.
print(szam[::-1])

for i in szam:
    print(str(i),end="")
print()

#3.
for i in range(len(szam)):
    print(szam[i],end=" ")
    if i%5==4:
        print()
#4
print()

osszeg=sum(szam)
print("A számok összege: ",osszeg)

print()

#5.
szoveg="Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."
print(szoveg)

#6 és 7.
betu=""
while betu != "fin":
    betu=str(input("Kérek egy betűt: "))
    if betu in szoveg:
        print(szoveg.index(betu))
    betu=input("Kell új betű? ")

#8.
szoveg2 = szoveg.split(".")
print(szoveg2[::-1])

print()
#9.
print("Szöveg méret: ",len(szoveg))

szoveg=szoveg.replace("a","")
szoveg=szoveg.replace("e","")
print(szoveg)

print("Szöveg mérete a és e betű nélkül: ",len(szoveg))

