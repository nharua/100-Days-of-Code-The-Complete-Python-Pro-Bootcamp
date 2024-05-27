from menu import MENU
from resources import RESOURCES

"""
Program requirements
1. Print report
2. Check resources sufficient?
3. Process coins.
4. Check transaction successful?
5. Make coffee.
"""


def check_resources(item):
    global MENU, RESOURCES
    result = True
    for i in MENU[item]["ingredients"]:
        if MENU[item]["ingredients"][i] <= RESOURCES[i]:
            result = result and True
        else:
            result = result and False
            print(f"Sorry there is not enough {i}.")
    return result


def update_resource(item):
    global MENU, RESOURCES
    for i in MENU[item]["ingredients"]:
        RESOURCES[i] = RESOURCES[i] - MENU[item]["ingredients"][i]


be_continue = True
money = 0
while be_continue:
    user_input = input(
        "What would you like? (espresso/latte/cappuccino/report or q to exit): "
    ).lower()
    if user_input == "report":
        print(f"Water: {RESOURCES['water']}")
        print(f"Milk: {RESOURCES['milk']}")
        print(f"Coffee: {RESOURCES['coffee']}")
        print(f"Money: ${money}")
    elif user_input == "q":
        be_continue = False
    else:
        if check_resources(user_input):
            price = MENU[user_input]["cost"]
            print(f"Please pay {price}. Insert your coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            user_pay = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            if user_pay < price:
                print("Sorry that's not enough money. Money refunded.")
            else:
                in_change = round(user_pay - price, 3)
                print(f"Here is ${in_change} in change")
                print(f"Here is your {user_input} ☕️. Enjoy")
                update_resource(user_input)
                money = money + price
