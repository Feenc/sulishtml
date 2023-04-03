import random
f=open("szavak.txt")
f.close


szavak = ["nokedli", "körte", "tipp", "macska", "kutya","python"]
szo = random.choice(szavak)
print(random.choice(szo))
print("Akasztófa játék <3")
#print("Készítők: Verbulecz Bence,Ivánczi Ferenc,Haraszti Marcell,Keszericze Ákos.")
rosszTalalat = 0
maxRosszTalalat = 6
tippeltBetu = []
also="_"

while rosszTalalat < maxRosszTalalat:
    display_szo = ""
    for betu in szo:
        if betu in tippeltBetu:
            display_szo += betu
        else:
            display_szo += also+" "
    if also not in display_szo:
        print("Gratulálok, nyertél!")
        print("A helyes szó:"+szo)
        break

    print(display_szo)
    tipp = input("Tippelj egy betűre: ")
        
    if tipp in tippeltBetu:
        print("Ezt a betűt már tippelted!")
    else:
        tippeltBetu.append(tipp)
        if tipp in szo:
            print("Gratulálok, ez a betű benne van a szóban!")
            
            
        else:
            print("Ez a betű nincs benne a szóban.")
            rosszTalalat += 1

    print("Hibás tippjeid száma: " + str(rosszTalalat))

    if rosszTalalat == maxRosszTalalat:
        print("Sajnos vesztettél. A szó: " + szo)

