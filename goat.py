input1 = int(input(""))
if input1 >= 1 and input1 <= 3:
	input2 = int(input(""))
if input2 >= 1 and input2 <= 3:
 	input3 = int(input(""))
if input3 >= 1 and input3 <= 3:
    if input1 != input2 and input1 != input3:
        print("Stay")
    if input1 == input2 or input1 == input3:
        print("Switch")