# A simple implementation of Conway's Game of Life,
# visualized using Tkinter

import tkinter as tk
import random
import numpy as np
import copy

WORLD_SIZE = 60
CELL_DIM = 15
REFRESH_TIME = 100
INITIAL_DENSITY = 0.6
step = 1

# Create a world of size WORLD_SIZE*WORLD_SIZE cells, where
# each cell has a likelihood INITIAL_DENSITY of being 'live'
def init_world():
    world=np.empty((WORLD_SIZE, WORLD_SIZE), dtype=bool)
    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            r = random.random()
            if r > INITIAL_DENSITY:
                world[i,j] = True
            else:
                world[i,j] = False
    return world

# Update each cell according to the state transition rules:
# Live cells with 2 or 3 neighbours remain live;
# Dead cells with 3 neighbours become live; and
# All other cells remain (or become) dead.
def update(before):
    after = np.copy(before)

    for row, col in np.ndindex(before.shape):
        cs = count_surrounding(row, col)
        if before[row][col] == True and cs < 2:
            after[row][col] = False
        elif before[row][col] == True and cs > 3:
            after[row][col] = False
        elif before[row][col] == False and cs == 3:
            after[row][col] = True
        else:
            after[row][col] = before[row][col]
    return after

# For the given cell at (row,col), count the number of neighbouring
# cells that are live. Use periodic boundary conditions.
def count_surrounding(row, col):
    count = 0
    rows = world.shape[0]
    cols = world.shape[1]
    for rr in [row-1,row,row+1]:
        if rr < 0:
            r = rows-1
        elif rr > rows-1:
            r = 0
        else:
            r = rr
        for cc in [col-1,col,col+1]:
            if cc < 0:
                c = cols-1
            elif cc > cols-1:
                c = 0
            else:
                c = cc
            if not (r == row and c == col):
                if world[r][c]:
                    if not ((rr != r or cc != c)):
                        count += 1
    return count

# Animate one timestep of the simulation, and start another animation to
# occur after REFRESH_TIME ms
def animation():
    global step, world
    step += 1
    world = update(world)
    display_world()
    root.after(REFRESH_TIME, animation)

# Display the current state of the world
def display_world():
    canvas.delete(tk.ALL)
    for x, y in np.ndindex(world.shape):
            rect = (x*CELL_DIM, y*CELL_DIM, (x+1)*CELL_DIM, (y+1)*CELL_DIM)
            if world[y][x]:
                canvas.create_rectangle(rect, outline="black", fill="orange")
            else:
                canvas.create_rectangle(rect, outline='darkblue')


world = init_world()

# Set up visualization window
root = tk.Tk()
root.title("Conway's Game of Life")
canvas = tk.Canvas(root, width=world.shape[1]*CELL_DIM + 1, height=world.shape[0]*CELL_DIM+1, bg='darkblue')
canvas.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

# Start animation
root.after(0, animation)
root.mainloop()
