print("Quizz játék <3")
kerdes=input("Készen állsz?(igen/nem): ")
print("-"*30)

pontok=0
kerdesek=5


if kerdes=="igen" or kerdes== "Igen":
    while kerdes=="nem" or kerdes== "Nem":
        break
    print("Ki dolgozott a legkevesebbet a projektel? ")
    valasz=input("A:Ákos "+"B:Marcell "+"C:Bence"+": ")
    while valasz not in ["c","C"]:
        print("Rossz válasz!")
        print("Pontjaid száma: {}".format(pontok))
        print("-"*30)
        break
    if valasz in ["c","C"]:
        print("Helyes válasz!")
        pontok+=1
        print("Pontjaid száma: {}".format(pontok))
        print("-"*30)
    print("Milyen állat a marabu? ")
    valasz=input("A:majom "+"B:madar "+"C:hal"+": ")
    while valasz not in ["b","B"]:
        print("Rossz válasz!")
        print("Pontjaid száma: {}".format(pontok))
        print("-"*30)
        break
    while valasz in ["b","B"]:
        print("Helyes válasz!")
        pontok+=1
        print("Pontjaid száma: {}".format(pontok))
        print("-"*30)
        break
    print("Ki volt a közepjorban az igric? ")
    valasz=input("A:Énekmondó "+"B:Udvaribolond "+"C:Orvos "+": ")
    while valasz not in ["a","A"]:
        print("Rossz válasz!")
        print("Pontjaid száma: {}".format(pontok))
        print("-"*30)
        break
    if valasz in ["a","A"]:
        print("Helyes válasz!")
        pontok+=1
        print("Pontjaid száma: {}".format(pontok))
        print("-"*30)
    print("Milyen hajszín lehet a platina? ")
    valasz=input("A:Barna "+"B:Szőke "+"C:Fekete "+": ")
    while valasz not in ["b","B"]:
        print("Rossz válasz!")
        print("Pontjaid száma: {}".format(pontok))
        print("-"*30)
        break
    if valasz in ["b","B"]:
        print("Helyes válasz!")
        pontok+=1
        print("Pontjaid száma: {}".format(pontok))
        print("-"*30)
    print("Melyik szélességi kőr következik az Északi sarkkör után? ")
    valasz=input("A:Ráktérítő "+"B:Baktérítő "+"C:Egyenlítő "+": ")
    while valasz not in ["a","A"]:
        print("Rossz válasz!")
        print("Pontjaid száma: {}".format(pontok))
        print("-"*30)
        break
    if valasz in ["a","A"]:
        print("Helyes válasz!")
        pontok+=1
        print("Pontjaid száma: {}".format(pontok))
        print("-"*30)
        print("Gratulálok! Elért pontjaid száma: 5/{}.".format(pontok))
        print("Elért százalék: {0:.0f}%".format(pontok/5*100))
        print("-"*30)
    

    
    
