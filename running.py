def unique_path(stairs):
    if stairs == 1:
         return 1
    if stairs == 2:
        return 2
    if stairs == len(stored_list):
        return stored_list[stairs]
    
    #Because the first and second stair will be fixed
    stored_list[1] = 1
    stored_list[2] = 2
    for i in range(3, stairs+1):
        # In case of 1 step and 2 step use recursion
        stored_list[i] = unique_path(i-1) + unique_path(i-2)
    
    return stored_list[stairs]


# Time for the code it's repeating
number_of_time = int(input())
results = []

# Add all the info to the results list
for _ in range(number_of_time):
    n = int(input())
    stored_list = [0] * (n+1)
    final = unique_path(n)
    results.append(final)

for result in results:
    print(result)