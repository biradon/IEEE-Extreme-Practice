import math

def find_destination_point(degree, hypotenuse):
    destination_point = []
    if degree == 0 or degree == 360:
        y = 0
        x = hypotenuse
    if degree == 90:   
        y = hypotenuse
        x = 0
    if degree == 180:
        x = -hypotenuse
        y = 0
    if degree == 270:  
        x = 0
        y = -hypotenuse
    if degree < 90:
        y = float(math.sin(math.radians(degree)) * hypotenuse)
        x = float(math.cos(math.radians(degree)) * hypotenuse)
    if degree > 91 and degree < 180:
        degree = 180 - degree
        y = (float(math.sin(math.radians(degree)) * hypotenuse))
        x = -(float(math.cos(math.radians(degree)) * hypotenuse))
    if degree > 181 and degree < 270:
        degree = 270 - degree
        y = -(float(math.sin(math.radians(degree)) * hypotenuse))
        x = -(float(math.cos(math.radians(degree)) * hypotenuse))
    if degree > 271 and degree <360:
        degree = 360 - degree
        y = -(float(math.sin(math.radians(degree)) * hypotenuse))
        x = (float(math.cos(math.radians(degree)) * hypotenuse))
    destination_point.append(round(x, 2))
    destination_point.append(round(y, 2))
    return destination_point


distance = float(input())
degree = float(input())

print(find_destination_point(degree, distance))