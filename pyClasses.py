class Point(object):
    def __init__(self, cordX, cordY):
        self.coordinateX = cordX
        self.coordinateY = cordY

    def __str__(self):
        return "({0},{1})".format(self.coordinateX, self.coordinateY)

    def __sub__(self, other):
        diffX = pow(self.coordinateX - other.coordinateX, 2)
        diffY = pow(self.coordinateY - other.coordinateY, 2)

        return  pow(diffX + diffY, 1/2)

    def modify(self, cordX, cordY):
        self.coordinateX = cordX
        self.coordinateY = cordY

    def getCoordinates(self) -> tuple:
        return (self.coordinateX, self.coordinateY)

class Line(Point):
    def __init__(self, pt1, pt2):
        self.pointA = pt1
        self.pointB = pt2

    def __str__(self):
        return "{}, {}".format(self.pointA, self.pointB)

    def getLength(self):
        return self.pointA - self.pointB

    def modify(self, pt1, pt2):
        self.pointA = pt1
        self.pointB = pt2

    def getPoints(self) -> tuple:
        return (self.pointA.getCoordinates(), self.pointB.getCoordinates())