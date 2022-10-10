beSzam=0

while beSzam<2 or beSzam>5 :
    beSzam= int(input("Adjon meg egy szamot 2 és 5 kozott: "))

autok=[]
for i in range(0, beSzam):
    autok.append(input ("Kérek egy auto markat: "))

print (autok)
