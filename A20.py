def convert_to_binary(user_input):
    converted_to_binary = []
    for char in user_input:
        for i in range(0,len(hexadecimal)):
            if char == hexadecimal[i]:
                converted_to_binary.append(binary[i])
    return converted_to_binary

def format_string_to_list(line):
    line = ''.join(line)
    line = list(line)
    return line

def check_A20_gate(formatted):
    i = 32
    while i > 0:
        if i == 11:
            A20 = int(formatted[i])
            if A20 > 0:
                A20 = A20 - 1
                formatted[i] = str(A20)
        i -= 1
    checked = ''.join(formatted)
    return checked

def convert_to_decimal(checked):
    final_result = []
    converted_to_decimal = [checked[i:i+4] for i in range(0, len(checked), 4)]
    for group in converted_to_decimal:
        for i in range(0, len(binary)):
            if group == binary[i]:
                final_result.append(hexadecimal[i])
    final_result = ''.join(final_result)
    return final_result

def check_duplicate(user_input, decimal_converted_result):
    return_result = []
    if decimal_converted_result == user_input:
        return_result.append(user_input)
    else:
        return_result.append(decimal_converted_result)
        return_result.append(user_input)
    return return_result



hexadecimal = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E', 'F']
binary = [
    '0000', # 0
    '0001', # 1
    '0010', # 2
    '0011', # 3
    '0100', # 4
    '0101', # 5
    '0110', # 6
    '0111', # 7
    '1000', # 8
    '1001', # 9
    '1010', # A
    '1011', # B
    '1100', # C
    '1101', # D
    '1110', # E
    '1111'  # F
]
converted_to_binary = []
original = []
final_final = []
print_out = []

# User input how many times to convert
times = int(input(""))

# Take user input and convert to binary
for i in range(times):
    user_input = input("").upper()
    converted_to_binary.append(convert_to_binary(user_input))
    for line in converted_to_binary:
        # Format string to list to compute
        formatted = format_string_to_list(line)
        # Check the location of gate A20
        checked = check_A20_gate(formatted)
        # Convert back from binary to decimal
        final = convert_to_decimal(checked)
    # Check if the number is not changed, return 1 result otherwise 2 result
    # At the same add the result to the list to print it out
    final_final.append(check_duplicate(user_input, final))

# Print the result out
for result in final_final:
    for converted in result:
        print(converted, end=" ")
    print("")

