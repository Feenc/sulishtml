"""
auto osztaly
par tulajdonsag:szin,ajtokszama,márka,tipus
tudjon indulni és akkor mondja hogy BRRRR
legyen rajta hangjelzes(duda)ami pl:tutu
iranyjelzo ami katkattkatt
egy leszarmazott ami bmw
induljon ugy hogy VRUM
iranyjelzo nema
masik leszarmazott mercedes neven
aminek mast mondjon a kurtje
3.auto ami audi
hamis check enginnel,de ha egyszer is megnyomjak a kurtot bekapcsol a check engine
"""

class auto(self,szin,ajtok,marka,tipus)
    def __init__(self,szin,ajtok,marka,tipus)
        self.szin=szin
        self.ajtok=ajtok
        self.marka=marka
        self.tipus=tipus
    def indulas(self)
        print("BRRR")
    def szin(self)
        print(f"Az autó színe {self.szin} )
              
auto1=("Kék",4,"Volkswagen","7R")
auto1.szin()
