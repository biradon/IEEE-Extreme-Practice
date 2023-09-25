input_str = input()
if len(input_str) <= 10 and len(input_str) > 0:
    if all(letter in input_str for letter in "BFTLC"):
        print("NO MISSING PARTS")
    else:
        if not "B" in input_str:
            print("B")
        if not "F" in input_str:
            print("F")
        if not "T" in input_str:
            print("T")
        if not "L" in input_str:
            print("L")
        if not "C" in input_str:
            print("C")