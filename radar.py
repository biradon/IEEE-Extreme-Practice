import math
# Function to fine the A,B,C in line
def line(x1, y1, x2, y2):
    A = y2 - y1
    B = x1 - x2
    C = y1*A - x1*B
    lineair.append(A)
    lineair.append(B)
    lineair.append(C)
    lineair.clear()  # Clear the list before appending new values
    lineair.extend([A, B, C])
    return lineair

# Function to find the distance
def distance(A,B,C,x1,y1):
    dis = (abs(A*x1 + B*y1 + C)) / (math.sqrt(A*A + B*B))
    return dis

# Function to find the destination point
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
        y = int(math.sin(math.radians(degree)) * hypotenuse)
        x = int(math.cos(math.radians(degree)) * hypotenuse)
    if degree > 91 and degree < 180:
        degree = 180 - degree
        y = (int(math.sin(math.radians(degree)) * hypotenuse))
        x = -(int(math.cos(math.radians(degree)) * hypotenuse))
    if degree > 181 and degree < 270:
        degree = 270 - degree
        y = -(int(math.sin(math.radians(degree)) * hypotenuse))
        x = -(int(math.cos(math.radians(degree)) * hypotenuse))
    if degree > 271 and degree <360:
        degree = 360 - degree
        y = -(int(math.sin(math.radians(degree)) * hypotenuse))
        x = (int(math.cos(math.radians(degree)) * hypotenuse))
    destination_point.append(x)
    destination_point.append(y)
    return destination_point

# Check the radar in the line of the flight or outside
def is_within_bounds(x, y, x1, y1, x2, y2):
    return (min(x1, x2) <= x <= max(x1, x2)) or (min(y1, y2) <= y <= max(y1, y2))

def is_touch_the_point(x1,y1,x2,y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance




lineair = []
nums = [] 
radars = []
count = 1
# Input the first line
nums = [int(char) for char in input().split(' ')] 

# Input the next line of radar info
for i in range(0, nums[2]):
    radars.append([int(char) for char in input().split(' ')]) 

# Find the destination point
destination_point = find_destination_point(nums[0], nums[1])

# Find A B C from function
line(0,0,destination_point[0],destination_point[1])


# Count the number of time
for radar in radars:
    # Find the distance
    result = distance(lineair[0], lineair[1], lineair[2], radar[0], radar[1])
    # Check if the distance is smaller than the range of the radar
    if is_within_bounds(radar[0], radar[1], destination_point[0],destination_point[1],0,0,):
        if result < radar[2]:
            count += 1
    else:
        compare_destination_point = is_touch_the_point(lineair[0], lineair[1], radar[0], radar[1])
        if compare_destination_point <= radar[2]:
            count += 1
        compare_start_point = is_touch_the_point(0, 0, radar[0], radar[1])
        if compare_start_point <= radar[2]:
            count += 1


print(f"The jet will appear on {count} radar screens.")
