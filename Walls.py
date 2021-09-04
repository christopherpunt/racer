from helpermethods import Line


class Walls():
    def __init__(self):
        self.walls = []
        self.setWalls()
        
    def setWalls(self):
        #outside
        self.walls.append(Wall(974,29,350,40))
        self.walls.append(Wall(350,40,297,71))
        self.walls.append(Wall(297,71,269,105))
        self.walls.append(Wall(269,105,210,359))
        self.walls.append(Wall(210,359,200,413))
        self.walls.append(Wall(200,413,218,601))
        self.walls.append(Wall(218,601,306,748))
        self.walls.append(Wall(306,748,553,828))
        self.walls.append(Wall(553,828,873,819))
        self.walls.append(Wall(873,819,1177,787))
        self.walls.append(Wall(1177,787,1223,736))
        self.walls.append(Wall(1223,736,1223,640))
        self.walls.append(Wall(1223,640,1170,577))
        self.walls.append(Wall(1170,577,1050,539))
        self.walls.append(Wall(1050,539,765,400))
        self.walls.append(Wall(765,400,1103,433))
        self.walls.append(Wall(1103,433,1259,538))
        self.walls.append(Wall(1259,538,1350,572))
        self.walls.append(Wall(1350,572,1458,583))
        self.walls.append(Wall(1458,583,1555,554))
        self.walls.append(Wall(1555,554,1622,515))
        self.walls.append(Wall(1622,515,1725,326))
        self.walls.append(Wall(1725,326,1692,124))
        self.walls.append(Wall(1692,124,1617,80))
        self.walls.append(Wall(1617,80,1520,34))
        self.walls.append(Wall(1520,34,974,29))

        #inside
        self.walls.append(Wall(1498,110,1007,111))
        self.walls.append(Wall(1007,111,411,120))
        self.walls.append(Wall(411,120,360,143))
        self.walls.append(Wall(360,143,331,179))
        self.walls.append(Wall(331,179,283,388))
        self.walls.append(Wall(283,388,282,571))
        self.walls.append(Wall(282,571,328,646))
        self.walls.append(Wall(328,646,368,686))
        self.walls.append(Wall(368,686,570,763))
        self.walls.append(Wall(570,763,1106,717))
        self.walls.append(Wall(1106,717,1118,677))
        self.walls.append(Wall(1118,677,1043,618))
        self.walls.append(Wall(1043,618,680,450))
        self.walls.append(Wall(680,450,616,395))
        self.walls.append(Wall(616,395,605,332))
        self.walls.append(Wall(605,332,634,297))
        self.walls.append(Wall(634,297,716,288))
        self.walls.append(Wall(716,288,1133,360))
        self.walls.append(Wall(1133,360,1315,485))
        self.walls.append(Wall(1315,485,1446,503))
        self.walls.append(Wall(1446,503,1525,488))
        self.walls.append(Wall(1525,488,1578,464))
        self.walls.append(Wall(1578,464,1658,301))
        self.walls.append(Wall(1658,301,1632,182))
        self.walls.append(Wall(1632,182,1498,110))

    def display(self):
        for wall in self.walls:
            wall.display()

class Wall():
    def __init__(self, x1, y1, x2, y2):
        self.hit = True
        self.line = Line(x1, y1, x2, y2) 

    def display(self):
        if (self.hit):
            self.line.turnRed()
        else:
            self.line.turnWhite()
        self.line.draw()
