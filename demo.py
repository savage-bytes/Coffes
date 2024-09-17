MENU = {
    "chai": {
        "ingredients": {
            "water": 50,
            "milk": 50,
            "coffee": 18
        },
        "cost": 10
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 18
        },
        "cost": 30
    },
    "hotcoffee": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 18
        },
        "cost": 20
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def is_resource_suff(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough

def is_transaction_success(money_received, charges):
    if money_received >= charges:
        change = round(money_received - charges, 2)
        print(f"Here is Rs{change} in change.")
        global profit
        profit += charges
        return True
    else:
        print("Sorry, that's not enough money.")
        return False
    
def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

def process_coins():
    print("Please insert coins.")
    total = int(input("How many 10 Coins? ")*100) 
    total += int(input("How many 5 Coins? ")*50) 
    return total

is_on = True

while is_on:
    choice = input("What would you like? (chai/latte/hotcoffee): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU.get(choice)
        if drink:
            if is_resource_suff(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_success(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.")


