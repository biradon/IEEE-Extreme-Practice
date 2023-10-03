# Create the menu
menu = [
    {"name": "A",
    "price": 5,
    "isVegeterian": False},
    {"name": "B",
    "price": 5,
    "isVegeterian": True},
    {"name": "C",
    "price": 2,
    "isVegeterian": False},
    {"name": "D",
    "price": 2,
    "isVegeterian": True},
]

# User input
B = int(input(""))
P = int(input(""))
Y = input("")

# Check have vegeterian friends or not
if Y == "Y":
    # Calculate maximum amount of Pizza can buy
    result1 = B / menu[1]["price"]
    result2 = B / menu[3]["price"]
    # Prioritize with B -> D
    if result1 - P >= 0:
        print(menu[1]["name"])
    elif result2 - P >= 0:
        print(menu[3]["name"])
    # If don't have enough money to buy
    else:
        print("NO PIZZA")
if Y == "N":
    # Calculate maximum amount of Pizza can buy
    result1 = B / menu[0]["price"]
    result2 = B / menu[1]["price"]
    result3 = B / menu[2]["price"]
    result4 = B / menu[3]["price"]
    # Prioritize with A -> B -> C -> D
    if result1 - P >= 0:
        print(menu[0]["name"])
    elif result2 - P >= 0:
        print(menu[1]["name"])
    elif result3 - P >= 0:
        print(menu[2]["name"])
    elif result4 - P >= 0:
        print(menu[3]["name"])
    # If don't have enough money to buy
    else:
        print("NO PIZZA")