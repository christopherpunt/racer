import pyglet
from Objects.Car import Car
from Objects.Walls import Walls
from Objects.CollisionDetector import CollisionDetector


class Game:
    def __init__(self):
        trackImg = pyglet.image.load('images/track.png')
        self.trackSprite = pyglet.sprite.Sprite(trackImg, x=0, y=0)

        self.walls = Walls()
        self.car = Car()

        self.CollisionDetector = CollisionDetector(self.car, self.walls.walls, self.car.vision.visionVectors)

    def render(self):
        self.trackSprite.draw()
        self.CollisionDetector.carWallCollisionDetection()
        self.CollisionDetector.visionWallCollisionDetection()
        self.walls.display()
        self.car.render()

