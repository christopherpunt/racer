

class CollisionDetector:
    def __init__(self, car, walls, visionVectors):
        self.car = car
        self.walls = walls
        self.visionVectors = visionVectors

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
            for vector in self.visionVectors:
                if vector.twoLinesCollided(wall.line):
                    wall.visionHit = True
                    break
                else:
                    wall.visionHit = False