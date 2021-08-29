from helpermethods import Line, Ray

class helperMethodsTests:
    def __init__(self):
        self.runTests()

    def runTests(self):
        self.lineTest()
        self.RayTests()

    def lineTest(self):
        line = Line(0,0,0,0)
        assert(line.getLength() == 0)

        line = Line(0,0,0,1)
        assert(line.getLength() == 1)
        print("lineTest Passed!")

    def RayTests(self):
        ray = Ray(0,0,360)
        assert(ray.getLength() == 300)

        ray2 = Ray(0,0,360)
        assert(ray2.getLength() == 300)
        print("rayTest Passed!")

    
