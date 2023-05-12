class telek:
    paros=False
    szelesseg=0
    kerites=""
    def __init__(self,sor):
        #sor: 1 8 K 
        vag=sor.replace("\n","").split(" ")
        if vag[0]==1:
            paros=False
        else:
            paros=True


telkek=[]
f=open("kerites.txt")
db=[]
for sor in f:
    telkek.append(telek(sor))

f.close
#t=telek("1 8 K")
print("2. Feladat")
print("Az eladott telkek száma {}".format(len(telkek)))
print("3. Feladat")
if telkek[-1].paros:
    print("A páros oldalon adták el.")
else:
    print("A páratlan oldalon adtál el.")
