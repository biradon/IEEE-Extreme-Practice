# This function is from neetcode channel
def calculate(triangle):
    dp = [0] * (len(triangle) + 1)

    for row in reversed(triangle):
        for i, n in enumerate(row):
            dp[i] = n + max(dp[i], dp[i+1])
    
    return dp[0]


# Take user input
user_input = int(input(""))
# Initial the array to store value
triangle = [[0 for _ in range(user_input)] for _ in range(user_input)]
for i in range(0, user_input):
    # Take user input
    temp = input("").split()
    for j in range(0, i+1):
        # Add user input to the array
        triangle[i][j] = int(temp[j])
print(calculate(triangle))



