nev=input("Kérek egy nevet")
print ("A " + nev + " nevet irtad be ")

print("A {belsoNev} nevet irtad be.".format(belsoNev=nev))


if len(nev)<5:
    print("Jó rövid név.")
elif len(nev)>=10:
    print("Very big név.")

be="nemvégjel"
szavak=[]
while be!="":
    be=input("irj be valamit")
    szavak.append(be)

#szavak.remove("")
#szavak.pop(len(szavak)-1)

print(szavak)
    
