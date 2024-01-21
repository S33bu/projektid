import tkinter as tk
from tkinter import Canvas
import random, math
import time



read = 20
veerud = 20

def loo_grid(read, veerud):
    return tk.Canvas(aken, bd=20)


aken = tk.Tk()
aken.geometry("650x650")
aken.title("Game of Life")
size_factor = 640 / 100


canvas = Canvas(width=640, height=640, bg = "white")
canvas.pack()
grid = [[0 for x in range(100)] for x in range(100)]

for x in range(100):
    for y in range (100):
        grid[x][y] = random.randint(0, 1)

def draw_square(x, y, size_factor):
        # Draw a square on the canvas.
        canvas.create_rectangle(x, y, x+size_factor, y+size_factor, fill='black', outline='black')

def algne_grid():
    for x in range(0, 100):
        for y in range(0, 100):
            realx = x * size_factor
            realy = y * size_factor
            if grid[x][y] == 1:
                draw_square(realx, realy, size_factor)

def mitu_naabrit(x, y):
    naabrid = 0

    xrange = [x-1, x, x+1]
    yrange = [y-1, y, y+1]

    for x1 in xrange:
        for y1 in yrange:
            if x1 == x and y1 == y:
                continue
            try:
                if grid[x1][y1] == 1:
                    naabrid += 1
            except:
                continue
    return naabrid

def main_mäng():
    uus_grid = [[0 for x in range(100)] for x in range(100)]

    for x in range(0, 100):
        for y in range(0, 100):
            naabrid = mitu_naabrit(x, y)
            if grid[x][y] == 1:
                if naabrid < 2:
                    uus_grid[x][y] = 0
                if naabrid == 2 or naabrid == 3:
                    uus_grid[x][y] = 1 #jääb ellu
                if naabrid > 3:
                    uus_grid[x][y] = 0
            else:
                if naabrid == 3:
                    uus_grid[x][y] = 1 #tuleb ellu
    return uus_grid

def uuenda():
    global grid
    canvas.delete("all")
    grid = main_mäng()
    algne_grid()
    aken.after(100, uuenda)
               

loo_grid(read, veerud)
algne_grid()
uuenda()
aken.mainloop()