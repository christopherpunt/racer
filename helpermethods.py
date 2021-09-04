from pyglet import shapes
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.point = shapes.Circle(self.x, self.y, 4)

    def draw(self):
        self.point.draw()

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.point1 = Point(x1, y1)
        self.point2 = Point(x2, y2)

        self.line = shapes.Line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, width=1)

    def twoLinesCollided(self, line):
        return self.linesCollided(self.point1.x, self.point1.y, self.point2.x, self.point2.y, line.point1.x, line.point1.y, line.point2.x, line.point2.y)

    def linesCollided(self, Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
        d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
        if d:
            uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
            uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
        else:
            return False
        if not(0 <= uA <= 1 and 0 <= uB <= 1):
            return False
        x = Ax1 + uA * (Ax2 - Ax1)
        y = Ay1 + uA * (Ay2 - Ay1)

        return x, y

    def turnRed(self):
        red = (255,0,0)
        self.line.color = red
    
    def turnWhite(self):
        white = (255,255,255)
        self.line.color = white

    def getLength(self):
        return math.sqrt( ((self.point2.x-self.point1.x)**2)+((self.point2.y-self.point1.y)**2) )        

    def draw(self):
        self.line.draw()
    
    def update(self, x1, y1, x2, y2):
        self.point1.x = x1
        self.point1.y = y1
        self.point2.x = x2
        self.point2.y = y2

        self.line.x = self.point1.x
        self.line.y = self.point1.y
        self.line.x2 = self.point2.x
        self.line.y2 = self.point2.y

class LineFromPoints(Line):
    def __init__(self, point1, point2):
        super().__init__(point1.x, point1.y, point2.x, point2.y)

class Ray(Line):
    def __init__(self, x, y, direction):
        self.length = 300
        Line.__init__(self, x, y, x + self.length * math.cos(math.radians(direction)), y + self.length * math.sin(math.radians(direction)))

    def update(self, x, y, direction):
        direction = direction
        Line.update(self, x, y, x + self.length * math.cos(math.radians(-direction)), y + self.length * math.sin(math.radians(-direction)))
