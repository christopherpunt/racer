from os import DirEntry
from pyglet import shapes
import math

class Vision:
    def __init__(self, carX, carY, carDirection):
        self.carX = carX
        self.carY = carY
        self.carDirection = carDirection

        self.forwardVector = Vector(self.carX, self.carY, self.carDirection + math.pi / 2)


    def draw(self):
        self.forwardVector.draw()

    def update(self, x, y, direction):
        self.forwardVector.x = x
        self.forwardVector.y = y
        self.forwardVector.direction = -direction + 90

class Vector:
    def __init__(self, x, y, direction):
        self.length = 300
        self.x = x
        self.y = y
        self.direction = direction
        self.line = shapes.Line(0,0,0,0)
    def draw(self):
        # self.direction = -self.direction + math.pi / 2
        self.line = shapes.Line(self.x, self.y, \
            self.x + self.length * math.cos(math.radians(self.direction)), \
            self.y + self.length * math.sin(math.radians(self.direction)), width=1)
        self.line.draw()