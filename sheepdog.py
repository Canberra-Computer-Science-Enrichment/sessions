import math
from math import pi
import random

import pygame
import os

# keyboard events
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    QUIT
)

WORLD_SIZE = 800
REFRESH_TIME = 800
NUM_SHEEP=100
SHEEP_SPEED = 3
DOG_SPEED = 6
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

    def passed_gate(self):
        return self.y <= 0 and (self.x > WORLD_SIZE/2-50) and self.x < (WORLD_SIZE/2+50)

    def update_position(self, bounce):
        self.x = self.x + self.speed * math.cos(self.direction)

        if self.x < 0:
            self.x = 0
            if bounce:
              self.direction += pi
            else:
              self.speed = 0
        elif self.x > WORLD_SIZE:
            self.x = WORLD_SIZE
            if bounce:
              self.direction -= pi
            else:
              self.speed = 0
        self.y = self.y + self.speed * math.sin(self.direction)
        if self.y < 0:               
            self.y = 0
            if bounce:
              self.direction += pi
            else:
              self.speed = 0
        elif self.y > WORLD_SIZE:
            self.y = WORLD_SIZE
            if bounce:
              self.direction -= pi
            else:
              self.speed = 0

class Sheep(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = SHEEP_SPEED

    def move(self):
        dx, dy = get_vector((self.x, self.y), (dog.x, dog.y))
        if dx*dx+dy*dy < DETECTION_RADIUS2:
            direction_to_dog = math.atan2(dy, dx)
            self.direction = direction_to_dog + pi
        elif random.random() < 0.2:
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
                    direction_to_s = math.atan2(vy, vx)
                    angle = abs(direction_to_s - self.direction)
                    if angle < pi / 4 or angle > 7 * pi / 4:
                        self.speed = 0
                        self.direction = (s.direction + self.direction) / 2
                    break
        self.update_position(True)

    def display(self):
        # head
        #canvas.create_oval(self.x-5, self.y-5, self.x+5, self.y+5, outline='darkgrey', fill='white')
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 5)
        # body
        points=[(0, -5), (0, 5), (-20, 5), (-20, -5)]
        points = [rotate_point(self.direction, p) for p in points]
        points = [(p[0]+self.x, p[1]+self.y) for p in points]
        pygame.draw.polygon(screen, 'white', points)
        pygame.draw.polygon(screen, 'lightgrey', points, 1)
        # tail
        points=[(-20, -4), (-20, 4), (-24, 0)]
        points = [rotate_point(self.direction, p) for p in points]
        points = [(p[0]+self.x, p[1]+self.y) for p in points]
        pygame.draw.polygon(screen, 'white', points)
        pygame.draw.polygon(screen, 'lightgrey', points, 1)

class Dog(Animal, pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 0
        # sprite
        #self.surf = pygame.image.load("C:\git\ccse\pygame\dog_sprite.png").convert()
        #self.surf.set_colorkey((255, 255, 255), pygame.locals.RLEACCEL)
        #self.rect = self.surf.get_rect()

    def display(self):
        # head
        points=[(0, -4), (5, -2), (5, 2), (0,4)]
        points = [rotate_point(self.direction, p) for p in points]
        points = [(p[0]+self.x, p[1]+self.y) for p in points]
        #pygame.draw.circle(screen, ('brown'), (self.x, self.y), 5)
        pygame.draw.polygon(screen, 'brown', points)
        # body
        points=[(0, -4), (0, 4), (-20, 4), (-20, -4)]
        points = [rotate_point(self.direction, p) for p in points]
        points = [(p[0]+self.x, p[1]+self.y) for p in points]
        pygame.draw.polygon(screen, 'darkorange', points)
        # tail
        points=[(-20, -2), (-20, 2), (-27, 0)]
        points = [rotate_point(self.direction, p) for p in points]
        points = [(p[0]+self.x, p[1]+self.y) for p in points]
        pygame.draw.polygon(screen, 'brown', points)

        # sprite
        #self.center = (self.x, self.y)
        #screen.blit(self.surf, self.center)

    def turn_left(self):
      self.direction -= pi / 32
      if self.direction > 2*pi:
          self.direction -= 2*pi
      elif self.direction < 0:
          self.direction += 2*pi
   
    def turn_right(self):
      self.direction += pi / 32
      if self.direction > 2*pi:
          self.direction -= 2*pi
      elif self.direction < 0:
          self.direction += 2*pi

def update():
    """
    Update the state of the world for the current timestep
    """
    global step, sheep
    step += 1

    dog.update_position(False)

    for s in sheep:
        s.move()
        if s.passed_gate():
            sheep.remove(s)

def display_world():
    """
    Display the current state of the world
    """
    # Fill the background with 'grass'
    screen.fill('forestgreen')
    pygame.draw.line(screen, 'black', [0,3], [WORLD_SIZE/2-50,3], width=3)
    pygame.draw.line(screen, 'black', [WORLD_SIZE/2+50,3], [WORLD_SIZE,3], width=5)

    # draw the animals to the screen
    dog.display()
    for s in sheep:
      s.display()

    img = font.render(str(len(sheep))+' sheep remaining', True, 'black')
    screen.blit(img, (20, 20))

# initialize the pygame library
pygame.init()
pygame.display.set_caption('Sheepdog')

# set up the drawing window
screen = pygame.display.set_mode([WORLD_SIZE, WORLD_SIZE])
clock = pygame.time.Clock()

# set up a font
font = pygame.font.SysFont(None, 24)

# create the animals
dog = Dog(WORLD_SIZE/2, WORLD_SIZE/2)
sheep = []
for i in range(NUM_SHEEP):
    sheep.append(Sheep(random.random()*WORLD_SIZE, random.random()*WORLD_SIZE))

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get the set of keys pressed and control the dog
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
      dog.turn_left()
    if pressed_keys[K_RIGHT]:
        dog.turn_right()
    if pressed_keys[K_UP]:
        dog.speed = min(DOG_SPEED, dog.speed+0.5)
    if pressed_keys[K_DOWN]:
        dog.speed = max(0, dog.speed-0.5)

    update()

    display_world()

    if len(sheep) == 0:
        font = pygame.font.SysFont(None, 80)
        img = font.render('You win!!', True, 'yellow')
        screen.blit(img, (280, 300))

    # Flip the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# Done! Time to quit.
pygame.quit()
