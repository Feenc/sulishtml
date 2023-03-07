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
for i in range(len(gyumolcs)):
    if len(gyumolcs[i])<5:
        print(gyumolcs[i])
