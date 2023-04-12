class BankFiok:
    def __init__(self, nev, cim):
        self.nev = nev
        self.cim = cim
        self.szamlak = []

    def uj_szamla(self, nev, egyenleg=0):
        szamla = Szamla(nev, egyenleg)
        self.szamlak.append(szamla)

    def osszes_szamla(self):
        for szamla in self.szamlak:
            print(szamla.nev)

class Szamla:
    def __init__(self, nev, egyenleg=0):
        self.nev = nev
        self.egyenleg = egyenleg

    def befizet(self, osszeg):
        self.egyenleg += osszeg

    def kivesz(self, osszeg):
        self.egyenleg -= osszeg

    def egyenleg_lekerdez(self):
        return self.egyenleg


fiok = BankFiok("BankFiok1", "Budapest, Kossuth Lajos utca 1.")
fiok.uj_szamla("Adam")
fiok.uj_szamla("Eva")
fiok.uj_szamla("Peter")

fiok.osszes_szamla()

szamla = fiok.szamlak[0]
szamla.befizet(5000)
print(szamla.egyenleg_lekerdez())
szamla.kivesz(2000)
print(szamla.egyenleg_lekerdez())
