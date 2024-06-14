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
}

cash = {
    "money": 0,
    "total_money_inserted": 0,
}

#Functions

def choose(selection):
    """
    Function that returns the choice of the person, it can be one of the following: espresso/latte/capuccino/off/report 
    """
    selection = input("What would you like? \n (espresso/latte/capuccino): ")
    return selection

def ingredients_check(selection):
    """
    Function that checks if there is available ingredients, and after that, updates the remaining qty of each, according to the user's selection
    """
    enough = True
    water_left = resources.get("water")
    coffee_left = resources.get("coffee")
    milk_left = resources.get("milk")
    if "water" in MENU[selection]["ingredients"]:
        water_needed = MENU[selection]["ingredients"]["water"]
        if water_left - water_needed < 0:
            enough = False
            print("Sorry, there's not enough water")
        else:
            left = water_left - water_needed
            resources.update({"water":left})
            
    if "coffee" in MENU[selection]["ingredients"]:
        coffee_needed = MENU[selection]["ingredients"]["coffee"]
        if coffee_left - coffee_needed < 0:
            enough = False
            print("Sorry, there's not enough coffee")
        else:
            left = coffee_left - coffee_needed
            resources.update({"coffee": left})    
    
    if "milk" in MENU[selection]["ingredients"]:
        milk_needed = MENU.get(selection)["ingredients"]["milk"]
        if milk_left - milk_needed < 0:
            enough = False
            print("Sorry, there's not enough milk")
        else:
            left = milk_left - milk_needed
            resources.update({"milk": left})
    return enough


def pay(selection):
    try:
        quarters = float(input("Please input the number of quarters you will insert: "))
    except ValueError:
        quarters = 0
    try:    
        dimes = float(input("Please input the number of dimes you will insert: "))
    except ValueError:
        dimes = 0
    try:        
        nickles = float(input("Please input the number of nickles you will insert: "))
    except ValueError:
        nickles = 0
    try:        
        pennies = float(input("Please input the number of pennies you will insert: "))
    except ValueError:
        pennies = 0
            
    if cash["total_money_inserted"] == 0:
        total = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    else:
        total = cash["total_money_inserted"] + 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    cash.update({"total_money_inserted":total})
    total_money = cash.get("total_money_inserted")
    price = MENU[selection]["cost"]

    if total_money > price:
        change = round(total_money - price,2)
        print(f"Here you have {change} in change, enjoy your {selection}!!")
        earnings =+ float(price) + cash["money"]
        cash.update({"money":earnings})
        cash.update({"total_money_inserted":0})
        return cash["money"],cash["total_money_inserted"]

    elif total_money < price:
        left = round(price-total_money,2)
        print(f"You are missing ${left}, please insert more coins")
        pay(selection)

def report():
    print("Water: ",resources["water"])
    print("Milk: ",resources["milk"])  
    print("Coffee: ",resources["coffee"])
    print("Money: ",cash["money"])


#START
poweroff = False
while poweroff == False:
    selection = input("What would you like? \n (espresso/latte/capuccino): ")
    if selection == "off":
        poweroff = True
    elif selection == "report":
        report()
    else:
        pay(selection)
        ingredients_check(selection)