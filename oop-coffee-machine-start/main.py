from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
money_machine=MoneyMachine()
coffee=CoffeeMaker()
should_continue=True
while should_continue:
    prompt=input(f"What would you like? ({menu.get_items()}): ")
    if prompt == "off":
        should_continue = False
    elif prompt=="report":
        coffee.report()
        money_machine.report()
    else:
        drink=menu.find_drink(prompt)
        if coffee.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee.make_coffee(drink)






