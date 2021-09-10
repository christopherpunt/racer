from Objects.Vision import Vision
from helpers.helpermethods import Line, LineFromPoints, Point
import pyglet
import math

class Car:
    START_POS_X = 250
    START_POS_Y = 250
    LENGTH = 40
    WIDTH = 20
    MAX_VELOCITY = 5
    MAX_ROTATION_VELOCITY = 5
    ACCELERATION = .1
    ROTATION_ACCELERATION = .3
    FRICTION = .1

    def __init__(self):
        #region carInit

        self.x = Car.START_POS_X
        self.y = Car.START_POS_Y
        self.velx = 0
        self.vely = 0
        self.width = Car.WIDTH
        self.length = Car.LENGTH
        self.direction = 0
        self.acceleration = 0
        self.velocity = 0
        self.rotationAcceleration = 0
        self.rotationVelocity = 0
        self.hit = False

        #endregion

        #region sides
        self.frontSide = Line(0,0,0,0)
        self.backSide = Line(0,0,0,0)
        self.leftSide = Line(0,0,0,0)
        self.rightSide = Line(0,0,0,0)
        self.sides = self.setSides()

        #endregion

        self.vision = Vision(self.x, self.y, self.direction)

        #pyglet defs
        self.carPic = pyglet.image.load("images/car.png")
        self.carSprite = pyglet.sprite.Sprite(self.carPic, x = self.x, y=self.y)
        self.carSprite.update(rotation=-90, scale_x=self.length / self.carSprite.width, scale_y=self.width / self.carSprite.height)
        #to center the rotation around the center of the car
        self.carSprite.image.anchor_x = self.carSprite.image.width / 2
        self.carSprite.image.anchor_y = self.carSprite.image.height / 2

        #moving booleans
        self.turningRight = False
        self.turningLeft = False
        self.accelerating = False
        self.reversing = False

    def setSides(self):
        FRcorner = Point(self.x + Car.WIDTH/2 * math.cos(math.radians(-self.direction)) + Car.LENGTH/2 * math.sin(math.radians(-self.direction)), \
            self.y + Car.WIDTH/2 * math.sin(math.radians(-self.direction)) - Car.LENGTH/2 * math.cos(math.radians(-self.direction)))

        FLcorner = Point(self.x - Car.WIDTH/2 * math.cos(math.radians(-self.direction)) + Car.LENGTH/2 * math.sin(math.radians(-self.direction)), \
            self.y - Car.WIDTH/2 * math.sin(math.radians(-self.direction)) - Car.LENGTH/2 * math.cos(math.radians(-self.direction)))

        BLcorner = Point(self.x - Car.WIDTH/2 * math.cos(math.radians(-self.direction)) - Car.LENGTH/2 * math.sin(math.radians(-self.direction)), \
            self.y - Car.WIDTH/2 * math.sin(math.radians(-self.direction)) + Car.LENGTH/2 * math.cos(math.radians(-self.direction)))

        BRcorner = Point(self.x + Car.WIDTH/2 * math.cos(math.radians(-self.direction)) - Car.LENGTH/2 * math.sin(math.radians(-self.direction)), \
            self.y + Car.WIDTH/2 * math.sin(math.radians(-self.direction)) + Car.LENGTH/2 * math.cos(math.radians(self.direction)))

        self.frontSide = LineFromPoints(FLcorner, FRcorner)
        self.backSide = LineFromPoints(BLcorner, BRcorner)
        self.leftSide = LineFromPoints(BLcorner, FLcorner)
        self.rightSide = LineFromPoints(BRcorner, FRcorner)
        self.sides = [self.frontSide, self.backSide, self.leftSide, self.rightSide]
        return self.sides

    def update(self):
        self.direction = ((self.carSprite.rotation + 90) % 360)

        self.setSides()
        self.updateControls()
        self.move()
        self.limitations()
        self.vision.update(self.x, self.y, self.direction - 90)

    def limitations(self):
        #limit velocity
        if self.velocity > Car.MAX_VELOCITY:
            self.velocity = Car.MAX_VELOCITY
        elif self.velocity < -Car.MAX_VELOCITY:
            self.velocity = -Car.MAX_VELOCITY

        #limit turining velocity
        if self.rotationVelocity > Car.MAX_ROTATION_VELOCITY:
            self.rotationVelocity = Car.MAX_ROTATION_VELOCITY
        elif self.rotationVelocity < -Car.MAX_ROTATION_VELOCITY:
            self.rotationVelocity = -Car.MAX_ROTATION_VELOCITY

    def move(self):
        #forwards and backwards motion
        self.velocity += self.acceleration
        self.velx = math.sin(self.direction * (math.pi / 180))
        self.vely = math.cos(self.direction * (math.pi / 180))
        self.x += self.velx * self.velocity
        self.y += self.vely * self.velocity

        #turning motion
        self.rotationVelocity += self.rotationAcceleration

        self.carSprite.rotation += self.rotationVelocity
        self.carSprite.update(x=self.x, y=self.y)

    def updateControls(self):
        #forwards and backwards movement
        if self.accelerating == True:
            self.acceleration = Car.ACCELERATION
        elif self.reversing == True:
            self.acceleration = -Car.ACCELERATION
        else:
            #friction
            if self.velocity > .1:
                self.acceleration = -Car.FRICTION
            elif self.velocity < -.1:
                self.acceleration = Car.FRICTION
            else:
                self.velocity = 0
                self.acceleration=0

        #turning movement 
        if self.turningLeft and self.velocity > 0:
            # self.rotationVelocity = -Car.MAX_ROTATION_VELOCITY
            self.rotationAcceleration = -Car.ROTATION_ACCELERATION
        elif self.turningRight and self.velocity > 0:
            # self.rotationVelocity = Car.MAX_ROTATION_VELOCITY
            self.rotationAcceleration = Car.ROTATION_ACCELERATION

        #turining is opposite when moving backwards
        elif self.turningRight and self.velocity < 0:
            # self.rotationVelocity = -Car.MAX_ROTATION_VELOCITY
            self.rotationAcceleration = -Car.ROTATION_ACCELERATION
        elif self.turningLeft and self.velocity < 0:
            # self.rotationVelocity = Car.MAX_ROTATION_VELOCITY
            self.rotationAcceleration = Car.ROTATION_ACCELERATION
        else:
            self.rotationAcceleration = 0
            self.rotationVelocity = 0

    def render(self):
        self.update()
        self.vision.draw()
        for side in self.sides:
            side.draw()
        self.carSprite.draw()
