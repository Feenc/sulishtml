def ido2mp():
    pass


#elso feladat

eredmenyek=[]

f=open("triatlon.txt")
for egySor in f:
    temp=egySor.replace("\n","").split(";")
    eredmenyek.append(temp)
    


f.close
eredmenyek.pop(0)
#print(eredmenyek)
#masodik feladat
print("2.feladat")
print("A versenyen [] versenyző indult".format(len(eredmenyek)))
#harmadik feladat
print("3.feladat")

