from tkinter import *
def eltol(pontok,x,y):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2==0:
            vissza.append(pont+x)
        else:
            vissza.append(pont+y)
    return vissza
def nagyit(pontok,meret=1):
    vissza=[]
    for pont in(pontok):
            vissza.append(pont*meret)
    return vissza

def forgat(pontok,szog):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2==0:
            x=pontok[i]*math.cos(math.radians(szog))-pontok
# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("1000x1000")

# Create a canvas widget
canvas=Canvas(win, width=500, height=500, bg='red')
canvas.pack(fill= BOTH, expand=1)
canvas.configure(bg="lightgray")
"""# Add a line in canvas widget
canvas.create_line(200,200,200,35, fill="green", width=5)
canvas.create_line(400,200,400,35, fill="blue", width=5)
canvas.create_line(400,40,200,40, fill="white", width=5)
"""
M =(0,0,20,0,60,40,70,40,110,0,130,0,130,110,0,110,20,20,60,60,70,60,110,20,110,110,20,110)
canvas.create_line(M, fill="red", width=1)

M2=eltol(M,100,-100)

canvas.create_line(M2, fill="red", width=1)

nev=[]
for i in range(5):
    nev.append(eltol(M,100*i,0))
for betu in nev:
    canvas.create_line(betu, fill="green", width=1)
win.mainloop()
canvas.create
