def switch_drink(drinks):
    drinker = {
        1: "Water",
        2: "Milk",
        3: "Juice",
        4: "Wine",
        5: "Pepsi",

    }
    return drinker.get(drinks, "Error. choice was not valid, here is your money back.")


drink = int(input("enter a number between 1 and 5  :"))
print(switch_drink(drink))
