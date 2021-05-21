# An agent-based model of a system of sheep herded by a dog

import math
from math import pi
import tkinter as tk
import random

WORLD_SIZE = 800
REFRESH_TIME = 100
NUM_SHEEP=100
SHEEP_SPEED = 8
DOG_SPEED = 10
DETECTION_RADIUS2 = 100*100
step = 1

def rotate_point(theta,point):
    return point[0]*math.cos(theta)-point[1]*math.sin(theta), \
           point[0]*math.sin(theta)+point[1]*math.cos(theta)

def get_vector(p1, p2):
    vx = p2[0] - p1[0]
    vy = p2[1] - p1[1]
    return (vx, vy)

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.random() * 2*pi
        self.speed = 0

    def update_position(self):
        self.x = self.x + self.speed * math.cos(self.direction)

        if self.x < 0:
            self.x = 0
            self.direction += pi
        elif self.x > WORLD_SIZE:
            self.x = WORLD_SIZE
            self.direction -= pi
        self.y = self.y + self.speed * math.sin(self.direction)
        if self.y < 0:               
            self.y = 0
            self.direction += pi
        elif self.y > WORLD_SIZE:
            self.y = WORLD_SIZE
            self.direction -= pi

class Sheep(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = SHEEP_SPEED

    def move(self):
        if random.random() < 0.2:
             # max quarter-turn per timestep
            self.direction += (random.random() * 0.5*pi - 0.25 * pi)
            if self.direction > 2*pi:
                self.direction -= 2*pi
            elif self.direction < 0:
                self.direction += 2*pi
        self.speed = SHEEP_SPEED
        for s in sheep:
            if s != self:
                vx, vy = get_vector((self.x, self.y), (s.x, s.y))
                if vx*vx+vy*vy < SHEEP_SPEED*SHEEP_SPEED:
                    # possible collision
                    direction_to_s = math.atan2(vy, vx)
                    angle = abs(direction_to_s - self.direction)
                    if angle < pi / 4 or angle > 7 * pi / 4:
                        self.speed = 0
                        self.direction = (s.direction + self.direction) / 2
        self.update_position()

    def display(self, canvas):
        # head
        canvas.create_oval(self.x-5, self.y-5, self.x+5, self.y+5, outline='darkgrey', fill='white')
        # body
        points=[(0, -5), (0, 5), (-20, 5), (-20, -5)]
        points = [rotate_point(self.direction, p) for p in points]
        points = [(p[0]+self.x, p[1]+self.y) for p in points]
        canvas.create_polygon(points, outline='lightgrey', fill='white')
        # tail
        points=[(-20, -4), (-20, 4), (-24, 0)]
        points = [rotate_point(self.direction, p) for p in points]
        points = [(p[0]+self.x, p[1]+self.y) for p in points]
        canvas.create_polygon(points, outline='lightgrey', fill='white')


class Dog(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = DOG_SPEED

    def display(self, canvas):
        # head
        points=[(0, -4), (5, -2), (5, 2), (0,4)]
        points = [rotate_point(self.direction, p) for p in points]
        points = [(p[0]+self.x, p[1]+self.y) for p in points]
        canvas.create_polygon(points, outline='brown', fill='brown')
        # body
        points=[(0, -4), (0, 4), (-20, 4), (-20, -4)]
        points = [rotate_point(self.direction, p) for p in points]
        points = [(p[0]+self.x, p[1]+self.y) for p in points]
        canvas.create_polygon(points, outline='brown', fill='darkorange')
        # tail
        points=[(-20, -2), (-20, 2), (-27, 0)]
        points = [rotate_point(self.direction, p) for p in points]
        points = [(p[0]+self.x, p[1]+self.y) for p in points]
        canvas.create_polygon(points, outline='brown', fill='brown')

    def move(self):
        if random.random() < 0.2:
            # max quarter-turn per timestep
            self.direction += (random.random() * 0.5*pi - 0.25 * pi)
            if self.direction > 2*pi:
                self.direction -= 2*pi
            elif self.direction < 0:
                self.direction += 2*pi
        self.update_position()

def update():
    """
    Update the state of the world for the current timestep
    """
    global step, sheep
    step += 1
    for s in sheep:
        s.move()

def display_world():
    """
    Display the current state of the world
    """
    canvas.delete(tk.ALL)
    #dog.display(canvas)
    for s in sheep:
        s.display(canvas)

def animation():
    """
    Animate one timestep of the simulation, and start another animation to
    occur after REFRESH_TIME ms
    """
    update()
    display_world()
    root.after(REFRESH_TIME, animation)

dog = Dog(WORLD_SIZE/2, WORLD_SIZE/2)
sheep = []
for i in range(NUM_SHEEP):
    sheep.append(Sheep(random.random()*WORLD_SIZE, random.random()*WORLD_SIZE))

# Set up visualization window
root = tk.Tk()
root.title("Sheepdog")
canvas = tk.Canvas(root, width=WORLD_SIZE, height=WORLD_SIZE, bg='green')
canvas.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

# Start animation
root.after(0, animation)
root.mainloop()
