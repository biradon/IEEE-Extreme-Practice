import math
# import sys

# number_of_bath_room = 3
# cost_of_black = 5
# cost_of_pink = 7

# total_black = 60
# total_pink = 43
# money = math.ceil((total_black/10))*cost_of_black + math.ceil((total_pink/10))*cost_of_pink
# print(money)




line = input("").split()

number_of_bath_room = int(line[0])
cost_of_black = int(line[1])
cost_of_pink = int(line[2])
total_black = 0
total_pink = 0

for _ in range(number_of_bath_room):
    number_of_mosaic = input("").split()
    total_black += int(number_of_mosaic[0])
    total_pink += int(number_of_mosaic[1])

money = math.ceil((total_black/10))*cost_of_black + math.ceil((total_pink/10))*cost_of_pink
print(money)
