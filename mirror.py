looptimes = int(input(""))
final_final = []
# # make sure it's less than or equal to 10
if looptimes <= 10 and isinstance(looptimes, int):
    # Number of line will be ask user to input
    for j in range(0, looptimes):
        final_result = []
        # user input in 1st line
        user_input = input("")
        # Take user input in the same line
        numbers = user_input.split()
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        # Check is the prime number or not
        if 0 < num1 <= 500 and 0 < num2 <= 500:
            # Apply Sieve of Eratosthenes
            prime_numbers = [True] * (num2+1)
            prime_numbers[0] = prime_numbers[1] = False
            p = 2
            while p * p < num2:
                if prime_numbers[p]:
                    for i in range(p*p, num2+1, p):
                        prime_numbers[i] = False
                p += 1
            # Add prime numbers into the list
            for k in range(num1, num2+1):
                if prime_numbers[k]:
                    final_result.append(k)
        final_final.append(final_result)
# Print the results
for m in range(0, looptimes):
    print(len(final_final[m]))