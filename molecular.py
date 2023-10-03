number = int(input(""))
# Check condition for number input
if number >= 1 and number <= 250:
    # Initialize the array of moleculars
    moleculars = ["Cl", "Br", "Xe", "Kr", "Si", "As", "Rn", "Ne", "He", "H", "C", "N", "O", "F", "P", "S", "I"]
    # Store the result in the array
    print_result = []
    for i in range(0, number):
        i = input("")
        result = i.split()
        # If all of the elements in the results is in moleculars
        if all(elem in moleculars for elem in result):
            print_result.append("Molecular!")
        else:
            print_result.append("Not molecular!")
    # Print the results out
    for i in range(0, number):
        print(print_result[i])

