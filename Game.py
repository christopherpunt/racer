import pygame
import pyglet
from Car import Car
from Walls import Walls
from CollisionDetector import CollisionDetector
from helpermethods import *

vec2 = pygame.math.Vector2

class Game:
    def __init__(self):
        trackImg = pyglet.image.load('images/track.png')
        self.trackSprite = pyglet.sprite.Sprite(trackImg, x=0, y=0)

        self.walls = Walls()
        self.car = Car()

        self.CollisionDetector = CollisionDetector(self.car, self.walls.walls)

    def render(self):
        self.trackSprite.draw()
        self.CollisionDetector.carWallCollisionDetection()
        self.walls.display()
        self.car.render()

