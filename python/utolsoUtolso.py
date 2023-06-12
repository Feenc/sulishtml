class enber:
    def __init__(self,nev,szuletes,evszam):
        self.nev=nev
        self.szuletes=szuletes
        self.evszam=evszam
    def hanyeves(self):
        print(self.evszam-self.szuletes)

ember1=enber("Tibi",1973,2023)
ember1.hanyeves()

f=open("emberek.txt","w")
f.write=("Béla,1988,2023")
f.write=("Marci,2003,2023")
f.write=("Furko,2006,2023")
f.write=("Laci,1988,2023")
f.close
