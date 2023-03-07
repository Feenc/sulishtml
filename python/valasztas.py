f=open("szavazatok.txt")
kepviselo=[]
for e in f:
    kepviselo.append(e.replace("\n","").split(" "))
##print(kepviselo)

print("A versenyen {} versenyző indult.".format(len(kepviselo)))

#nevek=[]
if len (kepviselo)==0:
    print("Ilyen nevű képviselő nem szerepel a nyílvántarásban!")
else:
    for e in kepviselo:
        print("{} szavazat: {}".format(e[2],e[1],))

f.close
