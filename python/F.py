
from tkinter import *
# create the horizontal line of the 'F'
x1 = 50
y1 = 50
x2 = 150
y2 = 50

# create the vertical line of the 'F'
x3 = 100
y3 = 50
x4 = 100
y4 = 150

# create the horizontal bar of the 'F'
x5 = 50
y5 = 100
x6 = 100
y6 = 100


# create a new tkinter window
root = Tk()

# create a canvas widget
canvas = Canvas(root, width=200, height=200)
canvas.pack()

# draw the 'F' shape using the coordinates above
canvas.create_line(x1, y1, x2, y2)
canvas.create_line(x3, y3, x4, y4)
canvas.create_line(x5, y5, x6, y6)

# start the tkinter event loop
root.mainloop()
