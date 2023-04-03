from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("1000x1000")

# Create a canvas widget
canvas=Canvas(win, width=500, height=500, bg='red')
canvas.pack(fill= BOTH, expand=1)

# Add a line in canvas widget
canvas.create_line(200,200,200,35, fill="green", width=5)
canvas.create_line(400,200,400,35, fill="blue", width=5)
canvas.create_line(400,40,200,40, fill="white", width=5)

win.mainloop()
