from pyglet import shapes
import math


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.line = shapes.Line(x1, y1, x2, y2, width=1)

    def linesCollided(self, line1, line2):
        pass

    def getLength(self):
        return math.sqrt( ((self.x2-self.x1)**2)+((self.y2-self.y1)**2) )        

    def draw(self):
        self.line.draw()
    
    def update(self, x1, y1, x2, y2):
        self.line.x = x1
        self.line.y = y1
        self.line.x2 = x2
        self.line.y2 = y2

class Ray(Line):
    def __init__(self, x, y, direction):
        self.length = 300
        Line.__init__(self, x, y, x + self.length * math.cos(math.radians(direction)), y + self.length * math.sin(math.radians(direction)))

    def update(self, x, y, direction):
        Line.update(self, x, y, x + self.length * math.cos(math.radians(-direction)), y + self.length * math.sin(math.radians(-direction)))


def linesCollided(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)

    return True