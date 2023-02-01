#olyan szoveges file ahol van 100.000 születési datum ami a normal középiskolas korosztályhoz tartozhat
import random
def datum():
   return (str(random.randint(2003,2008)) + "." + str(random.randint(1,12)) + "." + str(random.randint(1,31)))

f=open("szuletes.txt","w")
datumok=[]
def generate():
    return i=0
while i!=1:
    f.write(datum() + "." +"\n")
    i+=1

 
f.close()

