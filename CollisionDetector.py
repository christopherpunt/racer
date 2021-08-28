import math
from Car import Car
import helpermethods

class CollisionDetector:
    def __init__(self, car, walls, vision):
        self.car = car
        self.walls = walls
        self.vision = vision

    def carWallCollisionDetection(self):
            self.car.direction = -self.car.direction

            FRcornerX = self.car.x + Car.WIDTH/2 * math.cos(math.radians(self.car.direction)) - Car.LENGTH/2 * math.sin(math.radians(self.car.direction))
            FRcornerY = self.car.y + Car.WIDTH/2 * math.sin(math.radians(self.car.direction)) + Car.LENGTH/2 * math.cos(math.radians(self.car.direction))

            FLcornerX = self.car.x - Car.WIDTH/2 * math.cos(math.radians(self.car.direction)) - Car.LENGTH/2 * math.sin(math.radians(self.car.direction))
            FLcornerY = self.car.y - Car.WIDTH/2 * math.sin(math.radians(self.car.direction)) + Car.LENGTH/2 * math.cos(math.radians(self.car.direction))

            BLcornerX = self.car.x - Car.WIDTH/2 * math.cos(math.radians(self.car.direction)) + Car.LENGTH/2 * math.sin(math.radians(self.car.direction))
            BLcornerY = self.car.y - Car.WIDTH/2 * math.sin(math.radians(self.car.direction)) - Car.LENGTH/2 * math.cos(math.radians(self.car.direction))

            BRcornerX = self.car.x + Car.WIDTH/2 * math.cos(math.radians(self.car.direction)) + Car.LENGTH/2 * math.sin(math.radians(self.car.direction))
            BRcornerY = self.car.y + Car.WIDTH/2 * math.sin(math.radians(self.car.direction)) - Car.LENGTH/2 * math.cos(math.radians(self.car.direction))

            for wall in self.walls:

                #front line, left line, right line, back line
                if helpermethods.linesCollided(wall.x1, wall.y1, wall.x2, wall.y2, FLcornerX, FLcornerY, FRcornerX, FRcornerY) or \
                    helpermethods.linesCollided(wall.x1, wall.y1, wall.x2, wall.y2, FLcornerX, FLcornerY, BLcornerX, BLcornerY) or \
                    helpermethods.linesCollided(wall.x1, wall.y1, wall.x2, wall.y2, FRcornerX, FRcornerY, BRcornerX, BRcornerY) or \
                    helpermethods.linesCollided(wall.x1, wall.y1, wall.x2, wall.y2, BLcornerX, BLcornerY, BRcornerX, BRcornerY):
                    
                    if (wall.hit == False):
                        wall.hit = True
                else:
                    if (wall.hit == True):
                        wall.hit = False

    def visionWallCollisionDetection(self):
        for wall in self.walls:
            if (helpermethods.twoLinesCollided(self.vision.forwardVector, wall)):
                print("collision")

        