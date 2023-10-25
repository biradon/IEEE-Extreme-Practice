import sys

def custom_sort(person):
    return (person[1], person[0])

lines = []
number_of_line = int(input(""))
for _ in range(number_of_line):
    line = input().strip()
    lines.append(line)

while True:
    try:
        line = input().strip()
        lines.append(line)
    except EOFError:
        break




transport_list = []



for line in lines[1:number_of_line+1]:
    value = line.split(" ")
    transport_list.append((value[0],int(value[1])))


sorted_list = sorted(transport_list, key=custom_sort)


height_dict = {}

for index, (name, height) in enumerate(sorted_list, start = 1):
    if height not in height_dict:
        height_dict[height] = [index]
    else:
        height_dict[height].append(index)


for height, index in height_dict.items():
    names = [sorted_list[i-1][0] for i in index]
    print(f"{' '.join(names)} {min(index)} {max(index)}")