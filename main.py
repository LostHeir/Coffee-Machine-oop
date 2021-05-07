from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
espresso = MenuItem("espresso", 75, 0, 7, 1.2)
cappuccino = MenuItem("cappuccino", 125, 30, 10, 1.9)
latte = MenuItem("latte", 200, 100, 15, 2)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

exit_machine = False

while not exit_machine:
    user_input = input(f"What would you like? ({coffee_menu.get_items()}): ")
    if user_input == "end":
        exit_machine = True
        print("Shutting down...")
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        user_drink = coffee_menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(user_drink) and money_machine.make_payment(user_drink.cost):
            coffee_maker.make_coffee(user_drink)

