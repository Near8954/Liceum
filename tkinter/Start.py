import tkinter
from random import randint

def draw(event):
    d = randint(0, 600)
    c = randint(0, 600)
    v = randint(0, 600)
    canvas.create_oval((d, c), (d + v, c + v), fill='red')
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()