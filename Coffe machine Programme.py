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
    "coffee": 100,
    "money": 0
}
def enough_resources(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][ingredient]>resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True
def total_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_coins = round((quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01), 2)
    return total_coins
def enough_coins(coffee, total):
    if MENU[coffee]["cost"]>total:
        return False
    return True
def change(coffee,total):
    change=round((total-MENU[coffee]["cost"]),2)
    print( f"Here is ${change} dollars in change." )
def type_coffee(coffee):
    if coffee=="espresso":
        print("Here is your espresso ☕️. Enjoy!")
    elif coffee=="latte":
        print("Here is your latte ☕️. Enjoy!")
    else:
        print( "Here is your cappuccino  ☕️. Enjoy!")
def add_money(coffee):
    resources["money"]+=MENU[coffee]["cost"]
def remove_ingredients(coffee):
    if coffee=="espresso":
        resources["water"]-=MENU["espresso"]["ingredients"]["water"]
        resources["coffee"]-=MENU["espresso"]["ingredients"]["coffee"]
    else:
        for ingredient in MENU[coffee]["ingredients"]:
            resources[ingredient]-=MENU[coffee]["ingredients"][ingredient]
def make_coffee():
    prompt=input("What would you like? (espresso/latte/cappuccino): ")
    while prompt!="off":
        if prompt=="report":
            for thing in resources:
                print(f"{thing} : {resources[thing]}")
            prompt = input("What would you like? (espresso/latte/cappuccino): ")
        else:
            if enough_resources(prompt):
                total = total_coins()
                print(total)
                if enough_coins(prompt, total):
                    change(prompt, total)
                    type_coffee(prompt)
                    add_money(prompt)
                    remove_ingredients(prompt)
                    prompt = input("What would you like? (espresso/latte/cappuccino): ")
                else:
                    print("Sorry that's not enough money. Money refunded.")
                    prompt = input("What would you like? (espresso/latte/cappuccino): ")
            else:
                prompt = input("What would you like? (espresso/latte/cappuccino): ")
    return
make_coffee()

