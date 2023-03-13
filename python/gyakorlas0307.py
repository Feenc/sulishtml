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


