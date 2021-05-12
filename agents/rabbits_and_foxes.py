# An agent-based model of a ecological system of rabbits, foxes, and grass

import tkinter as tk
import random
import numpy as np
import itertools

WORLD_SIZE = 60
CELL_DIM = 15
REFRESH_TIME = 100
INITIAL_DENSITY_RABBITS = 0.5
INITIAL_DENSITY_FOXES = 0.03
MAX_GRASS = 5
MAX_HUNGER = 10

step = 1

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hunger = MAX_HUNGER / 2

class Rabbit(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def move_and_eat(self):
        """
        If the amount of grass in this rabbit's location is 1 or more,
        reduce the amount of grass by one, and reduce this rabbit's hunger
        level by 1 (to a minimum hunger level of 0).
        Otherwise, move to a random neighbouring empty location (or stay
        in the current location if there are no empty neighbouring
        locations), and increase this rabbit's hunger level by 1 (to a
        maximum hunger level of MAX_HUNGER).
        """
        empty_neighbours = get_empty_neighbours(self.x,self.y)
        new_location = random.choice(empty_neighbours)
        animals[self.x,self.y] = None
        animals[new_location] = self
        self.x = new_location[0]
        self.y = new_location[1]
        # FIXME eat, reproduce

class Fox(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move_and_eat(self):
        """
        Move to a neighbouring rabbit and consume it, or move at random.
        If there are rabbits in any of the neighbouring locations, choose
        a random neighbouring location containing a rabbit and move to it,
        and reduce this fox's hunger by 1 (to a minimum hunger level of 0).
        If there are no rabbits in any of the neighbouring locations, choose
        to move to a random empty neighbouring location, or stay in the
        current location, and increase this fox's hunger by 1 (to a maximum
        hunger level of MAX_HUNGER).
        """
        empty_neighbours = get_empty_neighbours(self.x,self.y)
        new_location = random.choice(empty_neighbours)
        animals[self.x,self.y] = None
        animals[new_location] = self
        self.x = new_location[0]
        self.y = new_location[1]
        # FIXME eat, reproduce

def init_world():
    """
    Create a world of size WORLD_SIZE*WORLD_SIZE locations, where
    each location has a likelihood INITIAL_DENSITY_RABBITS of containing a 
    rabbit,  or INITIAL_DENSITY_FOXES of containing a fox
    """
    animals=np.empty((WORLD_SIZE, WORLD_SIZE), dtype=Animal)
    grass=np.empty((WORLD_SIZE, WORLD_SIZE), dtype=int)
    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            r = random.random()
            if r < INITIAL_DENSITY_FOXES:
                animals[i,j] = Fox(i,j)
                survivors.append(animals[i,j])
            elif r < INITIAL_DENSITY_RABBITS:
                animals[i,j] = Rabbit(i,j)
                survivors.append(animals[i,j])
            grass[i,j] = random.randint(0,MAX_GRASS)
    return animals, grass

def update(animals, grass):
    """
    Update the world by making each animal move, eat, reproduce, and/or die
    First, each animal moves, eats, and reproduces (if possible) in order
    from oldest to youngest.
    Second, the amount of grass is increased by 1 in each square that does
    not contain an animal.
    Finally, any animal that has a hunger level of MAX_HUNGER is removed
    from the world (as it has starved to death).
    """
    for animal in survivors:
        animal.move_and_eat()
        # FIXME animals that have starved should die
    return animals, grass

def get_empty_neighbours(row, col):
    """
    return a list of all neighbouring locations that are currently empty
    """
    empty_neighbours = []
    rows = animals.shape[0]
    cols = animals.shape[1]
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
                if not animals[r][c] or (rr == r and cc == c):
                    empty_neighbours.append((r,c))
    return empty_neighbours

def count_neighbours(row, col, type):
    """
    For the given location at (row,col), count the number of neighbouring
    location that contain an animal of type "type". 
    """
    count = 0
    for r,c in get_neighbourhood(row, col):
        if not (r == row and c == col):
            if isinstance(animals[r][c], type):
                count += 1
    return count

def get_neighbourhood(row, col):
    """
    For a given row and column, get the indexes of neighbouring cells.
    Use periodic boundary conditions.
    """
    rows = animals.shape[0]
    cols = animals.shape[1]
    x_values = [rows-1 if row == 0 else row-1, row, 0 if row == rows-1 else row-1]
    y_values = [cols-1 if col == 0 else col-1, col, 0 if col == cols-1 else col-1]
    return itertools.product(x_values, y_values)

def animation():
    """
    Animate one timestep of the simulation, and start another animation to
    occur after REFRESH_TIME ms
    """
    global step, animals, grass
    step += 1
    animals, grass = update(animals, grass)
    display_world()
    root.after(REFRESH_TIME, animation)

def display_world():
    """
    Display the current state of the world
    """
    canvas.delete(tk.ALL)
    for x, y in np.ndindex(grass.shape):
            rect = (x*CELL_DIM, y*CELL_DIM, (x+1)*CELL_DIM, (y+1)*CELL_DIM)
            grass_amount = grass[x,y]
            grass_color = from_rgb(245 - 49 * grass_amount, 220 - 24 * grass_amount, 180 - 36 * grass_amount)
            
            if isinstance(animals[x,y], Rabbit):
                canvas.create_rectangle(rect, outline=grass_color, fill="white")
            elif isinstance(animals[x,y], Fox):
                canvas.create_rectangle(rect, outline=grass_color, fill="orange")
            else:
                canvas.create_rectangle(rect, outline=grass_color, fill=grass_color)

def from_rgb(r,g,b):
    """
    translate an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % (r,g,b) 


survivors = []
animals, grass = init_world()


# Set up visualization window
root = tk.Tk()
root.title("Rabbits and Foxes")
canvas = tk.Canvas(root, width=WORLD_SIZE*CELL_DIM + 1, height=WORLD_SIZE*CELL_DIM+1, bg='darkblue')
canvas.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

# Start animation
root.after(0, animation)
root.mainloop()
