from helpermethods import Ray


class Vision:
    def __init__(self, carX, carY, carDirection):
        self.carX = carX
        self.carY = carY
        self.carDirection = carDirection

        self.forwardVector = Ray(self.carX, self.carY, self.carDirection)

    def draw(self):
        self.forwardVector.draw()

    def update(self, x, y, direction):
        self.forwardVector.update(x, y, direction)
