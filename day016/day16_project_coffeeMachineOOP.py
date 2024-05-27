"""
Program requirements
1. Print report
2. Check resources sufficient?
3. Process coins.
4. Check transaction successful?
5. Make coffee.
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()
money_machine = MoneyMachine()

be_continue = True
money = 0
while be_continue:
    options = menu.get_items()
    user_input = input(f"What would you like? {options}report or 'q' to exit: ").lower()
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "q":
        be_continue = False
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
