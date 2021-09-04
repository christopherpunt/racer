

class CollisionDetector:
    def __init__(self, car, walls, vision):
        self.car = car
        self.walls = walls
        self.vision = vision

    def carWallCollisionDetection(self):
        for wall in self.walls:
            for side in self.car.sides:
                if side.twoLinesCollided(wall.line):
                    wall.carHit = True
                    break
                else:
                    wall.carHit = False

    def visionWallCollisionDetection(self):
        for wall in self.walls:
            if (wall.line.twoLinesCollided(self.vision.forwardVector)):
                wall.visionHit = True
            else:
                wall.visionHit = False