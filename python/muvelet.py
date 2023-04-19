"""
2szamot kap
legyen 4 függvénye
4alap müvelet 2 számmal
az értékét adja vissza a függvény
pl 1 es 2 van eltarolva akkor az osszead függvény adja vissza hogy 3
"""
class muvelet:
    def __init__(self,szam1,szam2):
        self.ertek1=szam1
        self.ertek2=szam2
    def osszeadas(self):
        return self.ertek1+self.ertek2
    def kivonas(self):
        return self.ertek1-self.ertek2
    def osztas(self):
        return self.ertek1/self.ertek2
    def szorzas(self):
        return self.ertek1*self.ertek2
if __name__=='__main__':
    q=muvelet(10,10)
    print(q.osszeadas())
    print(q.szorzas())
    q=muvelet(5,5)
    print(q.kivonas())
    q=muvelet(8,4)
    print(q.osztas())
"""    
Muvelet=muvelet(10,10)
print(muvelet.osszeadas())
print(muvelet.osztas())
"""
