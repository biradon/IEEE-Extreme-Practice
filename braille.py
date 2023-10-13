braille = [[["o."],[".."],[".."]], # A
           [["o."],["o."],[".."]], # B
           [["oo"],[".."],[".."]], # C
           [["oo"],[".o"],[".."]], # D
           [["o."],[".o"],[".."]], # E
           [["oo"],["o."],[".."]], # F
           [["oo"],["oo"],[".."]], # G
           [["o."],["oo"],[".."]], # H
           [[".o"],["o."],[".."]], # I
           [[".o"],["oo"],[".."]], # J
           [["o."],[".."],["o."]], # K
           [["o."],["o."],["o."]], # L
           [["oo"],[".."],["o."]], # M
           [["oo"],[".o"],["o."]], # N
           [["o."],[".o"],["o."]], # O
           [["oo"],["o."],["o."]], # P
           [["oo"],["oo"],["o."]], # Q
           [["o."],["oo"],["o."]], # R
           [[".o"],["o."],["o."]], # S
           [[".o"],["oo"],["o."]], # T
           [["o."],[".."],["oo"]], # U
           [["o."],["o."],["oo"]], # V
           [[".o"],["oo"],[".o"]], # W
           [["oo"],[".."],["oo"]], # X
           [["oo"],[".o"],["oo"]], # Y
           [["o."],[".o"],["oo"]], # Z
           [[".."],[".."],[".."]], # SPACE
           ]

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]


text = input("").upper()
if isinstance(text,str):
    # Print line 1 of braille
    for m in range(0,3):
        # Iterate through the input
        for i in range(0, len(text)):
            # If the character in text mathc with alphabet
            for j in range(0, len(alphabet)):
                # Take the index to convert to braille
                if text[i] == alphabet[j]:
                    result = ''.join(braille[j][m])
                    print(result, end="")
        # New line but the gap is smaller
        print("\n",end="")

