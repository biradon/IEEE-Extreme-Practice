import math

start_point = [0,0]
destination_point = []
y = int(math.sin(math.radians(60)) * 400)
x = -int((math.cos(math.radians(60)) * 400))
destination_point.append(x)
destination_point.append(y)
print(destination_point)
m = round((destination_point[1] - start_point[1]) / ((destination_point[0] - start_point[0])),2)
print(m)
abc = []
for i in range(0, destination_point[0]-1, -1):
    line = round(m * i,2)
    abc.append(list((i, line)))

print(abc)