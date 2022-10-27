#def csak akkor fut le ha levan zárva
def szamologep():
    jel = input(''' Válassz egy műveleti jelet:
 + = Összeadás
 - = Kivonás
 * = Szorzás
 / = Osztás
''')

    szam1 = int(input("Adja meg az első számot: "))
    szam2 = int(input("Adja me a második számot: "))

    if jel == "+" :
         print('{} + {} = '.format(szam1, szam2))
         print(szam1 + szam2)
    elif jel == "-" :
         print('{} - {} = '.format(szam1, szam2))
         print(szam1 - szam2)
    elif jel == "*" :
         print('{} * {} = '.format(szam1, szam2))
         print(szam1 * szam2)
    elif jel == "/" :
         print('{} : {} = '.format(szam1, szam2))
         print(szam1 / szam2)
    elif jel == "":
         print("Nem jó")
def ujraker():
    ujra = input("Szeretnél újra számolni? (i/n)")

    if ujra == "i":
        szamologep()
    elif ujra == "n":
        print("Csá")
    else:
        ujraker()

szamologep()
ujraker()
