import math

def find_destination_point(degree, hypotenuse):
    destination_point = []
    x = hypotenuse * math.cos(math.radians(degree))
    y = hypotenuse * math.sin(math.radians(degree))
    destination_point.append(round(x, 2))
    destination_point.append(round(y, 2))
    return destination_point

def find_distance(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

char_and_degree = []
points = [[0,0]]
result = 0

# first line of the input
distance = int(input())

i = 0
while i < 26:
    user_input = list(input().split(' '))
    add_to_list = {'char': user_input[0].upper(),
                'degree': float(user_input[1])
                }
    char_and_degree.append(add_to_list)
    i+= 1

# User input paragraph
paragraph = input().upper()

# Iretate every letter in the paragraph
for i in range(len(paragraph)):
    # First character
    if i == 0:
        for j in range(len(char_and_degree)):
            if paragraph[i] == char_and_degree[j]['char']:
                point = find_destination_point(char_and_degree[j]['degree'], distance)
                points.append(point)
    # From the second character check duplicate
    if i > 0:
        # If the last number is the same with the current number, skip
        if paragraph[i] == paragraph[i-1]:
            continue
        # If it's not the same calculate
        else:
            for j in range(len(char_and_degree)):
                if paragraph[i] == char_and_degree[j]['char']:
                    point = find_destination_point(char_and_degree[j]['degree'], distance)
                    points.append(point)

# Find the distance between 2 points
for i in range(len(points)):
    # If in the last point stop the loop
    if i == len(points) - 1:
        break
    else:
        result += find_distance(points[i][0], points[i][1], points[i+1][0], points[i+1][1])

print(math.ceil(result))
