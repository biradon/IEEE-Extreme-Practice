j = 0
final_result = []
while j < 5:
    user_input = list(input(""))
    i = 0
    while i < len(user_input):
        # If the element exist only 1 time in the list
        if user_input.count(user_input[i]) == 1:
            final_result.append(user_input[i])
            # Break the while loop
            i = len(user_input)
        i += 1
    j += 1

# Print the result
m = 0
while m < len(final_result):
    print(final_result[m])
    m += 1

        


