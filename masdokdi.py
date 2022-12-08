import math

def egyenlet (a,b,c):
    szöveg="0 = "
    if a!=0:
        szöveg+str(a)+"x²"

    if b>=0:
        szöveg+=" + "+str(b)+"x"
    elif b<0:
        szöveg+="  "+str(b)+"x"
    if c>=0:
        szöveg+=" + "+str(c)
    elif c<0:
        szöveg+="  "+str(c)
    return szöveg
    


a = int (input("a="))
b = int (input("b="))
c = int (input("c="))

diszkriminans=b*b-4*a*c
if diszkriminans<0:
    print("nincs megoldas")
elif diszkriminans==0:
    megoldas=-b /(2*a)
    print("1 megoldas: []".format(megoldas))
else:
    x1=(-b+math.sqrt(diszkriminans)) / (2*a)
    x2=(-b+math.sqrt(diszkriminans)) / (2*a)
    print("2 megoldas? x1:(),  x2:()".format (x1.x2))
print(egyenlet(a,b,c))
