import math

def PaintCalc(height, width):
    return math.ceil(((height * width)/5))


print("You need to buy " + str(PaintCalc(2,4)) +" paint cans")