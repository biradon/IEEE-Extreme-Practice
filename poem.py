# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy


rhyme_lines = get_number()
passage_lines = get_number()
rhyme_list = []
passage_list = []
result_list = []
for _ in range(rhyme_lines):
    rhyme_list.append(input(""))

print("")

for _ in range(passage_lines):
    passage_list.append(input(""))


for line in passage_list:
    for word in line[-1]:
        if word in rhyme_list[0]:
             result_list.append("A")



print(result_list)