looptimes = int(input(""))
# make sure it's less than or equal to 10
if looptimes <= 10 and isinstance(looptimes, int):
    final_result = []
    # Number of line will be ask user to input
    for j in range(0, looptimes):
        # user input in 1st line
        user_input = input("")
        # Take user input in the same line
        numbers = user_input.split()
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        prime_numbers = []
        # Check is the prime number or not
        if 0 < num1 < 500 and 0 < num2 < 500:
            for i in range (num1, num2):
                if i == 2:
                    prime_numbers.append(i)
                if i == 3:
                    prime_numbers.append(i)
                if i == 5:
                    prime_numbers.append(i)
                if i == 7:
                    prime_numbers.append(i)
                if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i != 1:
                    prime_numbers.append(i)
            # Add prime numbers into the list
            final_result.append(prime_numbers)
        # Print the results
    for m in range(0, len(final_result)):
        print(len(final_result[m]))