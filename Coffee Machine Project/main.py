MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,}


secret_word = True
resources["Money"] = 0
def process_coins():
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
while secret_word:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "off":
        secret_word = False
    else:
        if prompt == "report":
            for key, value in resources.items():
                print(f"{key}: {value}")
        elif prompt == "espresso":
            if resources["water"] >= 50 and resources["coffee"] >= 18:
                total = process_coins()
                if total < MENU["espresso"]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    resources["water"] -= 50
                    resources["coffee"] -= 18
                    resources["Money"] += MENU["espresso"]["cost"]
                    if total > MENU["espresso"]["cost"]:
                        change = total - MENU["espresso"]["cost"]
                        print(f"Here is ${round(change,2)} in change.")
                    print("Here is your espresso Enjoy!")

            elif resources["water"] < 50 and resources["coffee"] >= 18:
                print("Sorry there is not enough water")
            elif resources["water"] >= 50 and resources["coffee"] < 18:
                print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough water and coffee")

        elif prompt == "latte":
            if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
                total = process_coins()
                if total < MENU["latte"]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    resources["water"] -= 200
                    resources["milk"] -= 150
                    resources["coffee"] -= 24
                    resources["Money"] += MENU["latte"]["cost"]
                    if total > MENU["latte"]["cost"]:
                        change = total - MENU["latte"]["cost"]
                        print(f"Here is ${round(change,2)} in change.")
                    print("Here is your latte Enjoy!")

            elif resources["water"] < 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
                print("Sorry there is not enough water")
            elif resources["water"] >= 200 and resources["milk"] < 150 and resources["coffee"] < 24:
                print("Sorry there is not enough milk")
            elif resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] < 24:
                print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough water,milk and coffee")
        elif prompt == "cappuccino":
            if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
                total = process_coins()
                if total < MENU["cappuccino"]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    resources["water"] -= 250
                    resources["milk"] -= 100
                    resources["coffee"] -= 24
                    resources["Money"] += MENU["cappuccino"]["cost"]
                    if total > MENU["cappuccino"]["cost"]:
                        change = total - MENU["cappuccino"]["cost"]
                        print(f"Here is ${round(change,2)} in change.")
                    print("Here is your cappuccino Enjoy!")

            elif resources["water"] < 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
                print("Sorry there is not enough water")
            elif resources["water"] >= 250 and resources["milk"] < 100 and resources["coffee"] < 24:
                print("Sorry there is not enough milk")
            elif resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] < 24:
                print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough water,milk and coffee")




