storage = []
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
final_result = []
# Take user input
lines = int(input(""))
for line in range(0, lines):
    user_input = input("").upper()
    storage.append(user_input)

# Compare with the alphabet
for list in storage:
    # Initial and reset the array every time iteration 
    final = []
    result = [0] * 26
    # Check each character from user input
    for character in list:
        for i, n in enumerate(alphabet):
            if character == n:
                result[i] = n
    # Check the missing character
    for k,m in enumerate(alphabet):
        if result[k] == 0:
            final.append(m)
    # If in the missing character have any word, add to the array
    if any(final):
        final_result.append("missing " + ''.join(final).lower())
    else:
        final_result.append("pangram")
# Print the result
for i in range(lines):
    print(final_result[i])