class Myclass:
    x=5
    def megnovel(self,mennyivel=1):
        self.x+=mennyivel


""""
print(Myclass.x)
p1=Myclass()
print(p1.x)
p2=Myclass()
p2.x=1
print(p2.x)
p1.megnovel()
print(p1.x)
"""

class ember:
    def __init__(self,nev,kor):
        self.nev=nev
        self.kor=kor

    def eletkor(self):
        print(f"{self.kor} éves vagyok.")

    def neve(self):
        print(f"A nevem {self.nev}.")
ember1=ember("Bence","13")
ember1.eletkor()
ember1.neve()

class kutya:
    nev,fajta,agresszivitas,kor,szin=["","",0,0,""]
    def __init__(self,nev,fajta,agresszivitas,kor,szin):
        self.nev=nev
        self.fajta=fajta
        self.agresszvitas=agresszivitas
        self.kor=kor
        self.szin=szin

    def bemutatkozik(self):
        print(f"A nevem {self.nev}, {self.fajta} fajta kutya vagyok, {self.kor} éves és {self.szin} színű.")
    def talalkozas(self,masik):

        if self.agresszivitas>=masik.agresszivitas:
            print("Megöllek kutya!")
        else:
            print("Ne bánts, báttya!")
        if self.agresszivitas>5 or masik.agresszivitas>5:
            print("Szevasz, kutya!")
        else:
            print("Szia, báttya!")
    def __str__(self):
        return "{}, {}, ({})".format(self.nev,self.fajta,self.kor)
class kotorek(kutya):
    def bemutatkozik(self):
        print("{} a nevem, kutyaság a mindenem!".format(self.nev))
    def __init__(self,nev,fajta,ag,kor,szin,szemszin):
        super().__init__(nev,fajta,ag,kor,szin)
        self.szemszin=szemszin

kutya1=kutya("Bodri","Puli",6,9,"fekete")
kutya2=kutya("Fütyi","Golden Retriever",1,3,"világos barna")

kutya1.bemutatkozik()    
kutya2.talalkozas(kutya1)
kutya1.talalkozas(kutya2)

kotor1=kotorek("Füles","Tacskó",10,4,"barna","zöld")
kotor1.bemutatkozik()
print(kotor1.szemszin)
#print(kutya1.szemszin)
#kutya1.talalkozas(kotor1)
print(kutya1)
print(kotor1)






        
