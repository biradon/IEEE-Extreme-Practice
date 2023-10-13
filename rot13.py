alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
final_result = []
for time in range(0,5):
    user_input = input("")
    result = []   
    for character in user_input: 
        if character.isupper():
            for i, n in enumerate(alphabet_upper):
                if character == n:
                    if i < 13:
                        result.append(alphabet_upper[i+13])
                    else:
                        result.append(alphabet_upper[i+13-26])
        else:
            for i, n in enumerate(alphabet_lower):
                if character == n:
                    if i < 13:
                        result.append(alphabet_lower[i+13])
                    else:
                        result.append(alphabet_lower[i+13-26])
                if character not in alphabet_lower:
                    result.append(character)
                    break

    final_result.append(result)    

for i in range(0,5):
    print(''.join(final_result[i]))

