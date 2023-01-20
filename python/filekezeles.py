f=open("teszt.txt","w")
f.write("hello")
f.write("\n")
f.write("vilag")

f.close()

f=open("teszt.txt","r")

szoveg=f.read()

sorok=szoveg.split("\n")
print(sorok)

f.close()

f=open("teszt.txt","r")
sorok=[]
for sor in f:
    sorok.append(sor.replace("\n","").replace("\r","")    
    print(sor)
        
    
f.close
