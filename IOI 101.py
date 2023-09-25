input_str = input("Input here: ")
temp = list(input_str)
for i in range(len(input_str)):
    if input_str[i] == "0":
        temp[i] = "O"
    if input_str[i] == "1":
        temp[i] = "l"
    if input_str[i] == "3":
        temp[i] = "E"
    if input_str[i] == "4":
        temp[i] = "A"
    if input_str[i] == "5":
        temp[i] = "S"
    if input_str[i] == "6":
        temp[i] = "G"
    if input_str[i] == "8":
        temp[i] = "B"
    if input_str[i] == "9":
        temp[i] = "g"
temp = ''.join(temp)
print(temp)