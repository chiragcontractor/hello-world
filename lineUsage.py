from pyClasses import Point, Line

def expandPoints(aTuple):
    points = []
    for m in aTuple:
        for i in m:
            points.append(i)

    return points


line1 = Line(Point(2,3), Point(2,7))
line2 = Line(Point(2,3), Point(5, 4))

print("Line A: {}".format(line1))
print("Length: {}".format(round(line1.getLength(), 2)))
print("Coordinates: {}".format(line1.getPoints()))

print("Line B: {}".format(line2))
print("Length: {}".format(round(line2.getLength(), 2)))
print("Coordinates: {}".format(line2.getPoints()))

print(expandPoints(line2.getPoints()))