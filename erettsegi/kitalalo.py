import modul
f=open("szavak.txt")
lista=[]
for e in f:
    lista.append(e.replace('"',"").strip().split(", ",""))
print(lista)
f.close
    
