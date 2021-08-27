import math
from Car import Car
import helpermethods

class CollisionDetector:
    def __init__(self, car, walls):
        self.car = car
        self.walls = walls

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

            # FRcircle = shapes.Circle(FRcornerX, FRcornerY, 5, color=(255,0,0))
            # FLcircle = shapes.Circle(FLcornerX, FLcornerY, 5, color=(255,0,0))
            # BRcircle = shapes.Circle(BRcornerX, BRcornerY, 5, color=(255,0,0))
            # BLcircle = shapes.Circle(BLcornerX, BLcornerY, 5, color=(255,0,0))

            # FRcircle.draw()
            # FLcircle.draw()
            # BRcircle.draw()
            # BLcircle.draw()

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
                    # return False