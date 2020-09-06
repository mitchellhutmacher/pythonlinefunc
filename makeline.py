def linemaker(pointone, pointtwo, x):
    slope = (pointone[1] - pointtwo[1])/(pointone[0] - pointtwo[0])
    y_int = pointone[1] - slope*pointone[0]
    return x*slope + y_int
