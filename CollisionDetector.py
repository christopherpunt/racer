

class CollisionDetector:
    def __init__(self, car, walls, vision):
        self.car = car
        self.walls = walls
        self.vision = vision

    def carWallCollisionDetection(self):
        for wall in self.walls:
            if (self.car.sides[0].twoLinesCollided(wall.line) or \
            self.car.sides[1].twoLinesCollided(wall.line) or \
            self.car.sides[2].twoLinesCollided(wall.line) or \
            self.car.sides[3].twoLinesCollided(wall.line)):
                wall.hit = True
            else:
                wall.hit = False

    def visionWallCollisionDetection(self):
        for wall in self.walls:
            if (wall.line.twoLinesCollided(self.vision.forwardVector)):
                wall.hit = True
            else:
                wall.hit = False