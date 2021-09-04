from helpermethods import Ray


class Vision:
    def __init__(self, carX, carY, carDirection):
        self.carX = carX
        self.carY = carY
        self.carDirection = carDirection

        self.forwardVector = Ray(self.carX, self.carY, self.carDirection)
        self.backVector = Ray(self.carX, self.carY, self.carDirection + 180)
        self.visionVectors = [self.forwardVector, self.backVector]

    def draw(self):
        for vector in self.visionVectors:
            vector.draw()

    def update(self, x, y, direction):
        # for vector in self.visionVectors:
        #     vector.update(x, y, direction)
        self.forwardVector.update(x, y, direction)
        self.backVector.update(x, y, direction + 180)