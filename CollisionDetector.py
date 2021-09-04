

class CollisionDetector:
    def __init__(self, car, walls, visionVectors):
        self.car = car
        self.walls = walls
        self.visionVectors = visionVectors

    def carWallCollisionDetection(self):
        for wall in self.walls:
            wall.carHit = False
            for side in self.car.sides:
                if side.twoLinesCollided(wall.line):
                    wall.carHit = True
                    break

    def visionWallCollisionDetection(self):
        for wall in self.walls:
            wall.visionHit = False
            for vector in self.visionVectors:
                intersection = vector.twoLinesCollided(wall.line)
                if intersection:
                    wall.visionHit = True
                    intersection.draw()
                    break