f=open("jarmu.txt")
jarmuvek=[]
for e in f:
     jarmuvek.append(e.replace("\n","").split(" "))
print(jarmuvek)

f.close
