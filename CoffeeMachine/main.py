

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
profit = 0
is_on = True

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coins():
    total = int(input("How many quarters? "))*0.25
    total += int(input("How many dimes? "))*0.1
    total += int(input("How many nickles? "))*0.05
    total += int(input("How many pennies? "))*0.01
    return total


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry, that's not enough money. Money returned.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True


def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order} ☕ Enjoy!")


while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif order == ('espresso' or 'latte' or 'cappuccino'):
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            if is_transaction_successful(process_coins(), drink["cost"]):
                make_coffee(drink["ingredients"])
    else:
        print(f"Sorry, we don't serve {order}.")
