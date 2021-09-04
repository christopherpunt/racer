from helpermethods import Ray


class Vision:
    def __init__(self, carX, carY, carDirection):
        self.carX = carX
        self.carY = carY
        self.carDirection = carDirection

        self.forwardVector = Ray(self.carX, self.carY, self.carDirection)
        self.backVector = Ray(self.carX, self.carY, self.carDirection + 180)
        self.rightVector = Ray(self.carX, self.carY, self.carDirection + 90)
        self.leftVector = Ray(self.carX, self.carY, self.carDirection - 90)
        self.visionVectors = {
            self.forwardVector : 0, 
            self.backVector : 180, 
            self.rightVector: 90,
            self.leftVector: -90
        }

    def draw(self):
        for vector in self.visionVectors:
            vector.draw()

    def update(self, x, y, direction):
        for vector in self.visionVectors:
            vector.update(x, y, direction + self.visionVectors[vector])