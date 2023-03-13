def oszlopVissza(hanyadik):
    oszlop=[]
    for e in tabla:
        oszlop.append(e[hanyadik-1])

    return oszlop
def proba(hanyadik):
    asd=[e[hanyadik-1::hanyadik]for e in tabla]
    return asd
gyumolcs=["alma","szolo","körte","barac","dragonfruit","licsi"]
print("Ennyi gyümölcs van: {}".format(len(gyumolcs)))
#print(gyumolcs[3])
#gyumolcs[3]+="k"
#gyumolcs[3]="barack"
print(gyumolcs.index("barac"))
#gyumolcs[gyumolcs.index("barac")]+="k"
index=gyumolcs.index("barac")
gyumolcs[index]+="k"
print(gyumolcs[3])

print("Rövid gyümölcsök: ")


#for i in range(len(gyumolcs)):
#    if len(gyumolcs[i])<5:
#        print(gyumolcs[i])

rovid=[]
for i in range(len(gyumolcs)):
    if len(gyumolcs[i])<5:
        rovid.append(gyumolcs[i])
print(rovid)

rovid=[]
for e in gyumolcs:
    if len(e)<5:
        rovid.append(e)

print(rovid)

rovid=[e for e in gyumolcs if len(e)<5]
print(rovid)

rovid=[]

i=0

while i<len(gyumolcs):
    if len(gyumolcs[i])<5:
        rovid.append(gyumolcs[i])
    i+=1
print(rovid)

rovid=[]
i=0
while True:
    print(i)
    if len(gyumolcs[i])<5:
        rovid.append(gyumolcs[i])

    if len(gyumolcs)-1==i:
        break
    i+=1
print(gyumolcs[:2])

print(gyumolcs[-2:])

print(gyumolcs[len(gyumolcs)-2:])

print(gyumolcs[1:-1])

paratlan=gyumolcs[1::2]
print(paratlan)
paros=gyumolcs[0::2]
print(paros)

masolat=gyumolcs
masolat.reverse()
print(",".join(masolat))

print(",".join(masolat[:]))


tabla=[]
for i in range(20):
    sor=[]
    for k in range(10):
        sor.append((i+1)*(k+1))
    tabla.append(sor)

#print(tabla)

oszlop=[]
for e in tabla:
    oszlop.append(e[0])

print(oszlop)
print(oszlopVissza(5))
print(oszlopVissza(6))
oszlop=[e[:3]for e in tabla]
oszlop=[e[4:7]for e in tabla]
oszlop=[e[3::4]for e in tabla]
#csinaljatok egy fuggvenyt ami megadja hogy hannyal oszthato
#bekeres ami megad egy szamot ami az annyival oszthato szamot adjaki
#3,7,1
szam = int(input("Adj meg egy szamot: "))

print("Azok a számok amelyek oszthatóak a " + str(szam) + "-val:")

for i in range(1, 20):
    if i % szam == 0:
        print(i)
#print(oszlop)


print(proba(int(input("Kérek egy szamot: "))))
oszlop=[[e[2],e[6],e[0]]for e in tabla]












