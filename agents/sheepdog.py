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
DETECTION_RADIUS2 = 200**2
MAX_TURN = 0.1
step = 1

cookie = None # a dog
sheep = [] # a list of sheep

def rotate_point(theta,point):
    """rotate a point(x,y) about the origin by angle theta"""
    return point[0]*math.cos(theta)-point[1]*math.sin(theta), \
           point[0]*math.sin(theta)+point[1]*math.cos(theta)

def get_vector(p1, p2):
    """calculate the vector from point p1 to point p2"""
    vx = p2[0] - p1[0]
    vy = p2[1] - p1[1]
    return (vx, vy)

def limit(x, minimum, maximum):
    """constrain a value x within the range [minimum,maximum]"""
    if x > maximum:
        return maximum
    elif x < minimum:
        return minimum
    return x

class Animal:
    """An animal that can move around the world.

    An Animal has a position (x,y), direction, and speed.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.random() * 2*pi
        self.speed = 0

    def update_position(self):
        """update the position of this animal based on the current direction and speed"""
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
        """determine direction and speed, and then move accordingly"""
        vx,vy = get_vector((cookie.x, cookie.y), (self.x, self.y))
        if vx**2 + vy**2 < DETECTION_RADIUS2:
            # sheep is within detection radius of dog - run away!
            self.speed = SHEEP_SPEED
            self.direction = math.atan2(vy, vx)
        else:
            # move randomly
            turn = (random.random() * 2*pi - pi) * MAX_TURN
            self.direction += turn
            acceleration = random.randint(-1,1)
            self.speed = limit(self.speed+acceleration, 0, SHEEP_SPEED)

        self.update_position()

    def display(self, canvas):
        """display this sheep on the canvas"""
        # head
        canvas.create_oval(self.x-5, self.y-5, self.x+5, self.y+5, outline='darkgrey', fill='white')
        # body
        points=[(0, -5), (0, 5), (-20, 5), (-20, -5)]
        rotated_points = [rotate_point(self.direction, p) for p in points]
        translated_points = [(p[0]+self.x, p[1]+self.y) for p in rotated_points]
        canvas.create_polygon(translated_points, outline='lightgrey', fill='white')
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
        """display this dog on the canvas"""
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
        """determine direction and speed, and then move accordingly"""
        turn = (random.random() * 2*pi - pi) * MAX_TURN
        self.direction += turn
        acceleration = random.randint(-1,1)
        self.speed = limit(self.speed+acceleration, 0, DOG_SPEED)
        self.update_position()

def update():
    """update the state of the world for the current timestep"""
    global step, sheep
    step += 1
    cookie.move()
    for s in sheep:
        s.move()

def display_world():
    """display the current state of the world"""
    canvas.delete(tk.ALL)
    cookie.display(canvas)
    for s in sheep:
        s.display(canvas)

def animation():
    """Animate one timestep of the simulation.
    
    After animating, start another animation to occur after REFRESH_TIME ms.
    """

    update()
    display_world()
    root.after(REFRESH_TIME, animation)

cookie = Dog(x=WORLD_SIZE/2, y=WORLD_SIZE/2)
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
