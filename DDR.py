a, b, c = input("").upper()
if a.isalpha() and b.isalpha() and c.isalpha():
    matrix = [[0 for _ in range(3)] for _ in range(3)]

    # Up and Down
    matrix[0][1] = "U";
    matrix[2][1] = "D";

    # Left and Right
    matrix[1][0] = "L";
    matrix[1][2] = "R";

    if ((matrix[1][0] == a and matrix[1][2] == c) and (b != matrix[1][0] and b != matrix[1][2])) or ((matrix[1][2] == a and matrix[1][0] == c) and (b != matrix[1][0] and b != matrix[1][2])): 
        print("Crossover")
    elif ((matrix[0][1] == a and matrix[2][1] == c) and (b != matrix[0][1] and b != matrix[2][1])) or ((matrix[2][1] == a and matrix[0][1] == c) and (b != matrix[0][1] and b != matrix[2][1])):
        print("Candle")
    else:
        print("Neither")


