# Convert decimal to binary
def decimal_to_binary(decimal):
    done = True
    binary = []
    temp = decimal * 2
    # handle 0 cas
    if temp == 0:
        binary.append(temp)
    while done:
        temp = temp // 2  
        remain = temp % 2
        if temp != 0:
            binary.append(remain)
        elif temp == 0:
            binary.reverse()
            done = False      
    # Make sure the length of the array is divisible by 4 
    while len(binary) % 4 != 0:
        binary.insert(0, 0)

    # Group the binary digits into sets of four
    grouped_binary = [binary[i:i+4] for i in range(0, len(binary), 4)]

    # Convert the grouped binary digits back to a string
    binary_string = ' '.join([''.join(map(str, group)) for group in grouped_binary])
    return binary_string


times = int(input(""))
printout = []
for i in range(0, times):
    decimal = int(input(""))
    printout.append(decimal_to_binary(decimal))
for i in range(0, len(printout)):
    print(printout[i])








