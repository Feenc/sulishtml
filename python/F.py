from tkinter import *

# create a new tkinter window
root = Tk()

# create a canvas widget
canvas = Canvas(root, width=300, height=200)
canvas.pack()

# create the 'f' using four line segments
canvas.create_line(50, 50, 50, 150)
canvas.create_line(50, 50, 100, 50)
canvas.create_line(50, 100, 100, 100)
canvas.create_line(50, 150, 100, 150)

# create the 'u' using three line segments
canvas.create_line(120, 50, 120, 150)
canvas.create_line(120, 50, 170, 50)
canvas.create_line(120, 150, 170, 150)
canvas.create_line(170, 50, 170, 150)

# create the 'r' using four line segments
canvas.create_line(190, 50, 190, 150)
canvas.create_line(190, 50, 240, 50)
canvas.create_line(240, 50, 240, 100)
canvas.create_line(240, 100, 190, 100)
canvas.create_line(190, 100, 240, 150)

# create the 'k' using four line segments
canvas.create_line(260, 50, 260, 150)
canvas.create_line(260, 100, 300, 50)
canvas.create_line(260, 100, 300, 150)
canvas.create_line(280, 100, 300, 100)

# create the 'o' using one oval shape
canvas.create_oval(330, 50, 370, 150)

# start the tkinter event loop
root.mainloop()
