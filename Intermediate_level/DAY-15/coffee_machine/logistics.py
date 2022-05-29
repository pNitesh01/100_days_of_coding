from kitchen import MENU, resources

money_left = 0

def get_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money_left}")


def is_resource_sufficient(coffee):
    water_quantity = MENU[coffee]['ingredients']['water']
    coffee_quantity = MENU[coffee]['ingredients']['coffee']
    milk_quantity = MENU[coffee]['ingredients']['milk']
    
    if resources['water'] < water_quantity:
        print("Sorry there is not enough water.")
    elif resources['coffee'] < coffee_quantity:
        print("Sorry there is not enough coffee.")
    elif resources['milk'] < milk_quantity:
        print("Sorry there is not enough milk.")
    else:
        return True
    return False 


def process_coins(coffee):
    global money_left
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    cost = MENU[coffee]['cost']
    
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        money_left += cost
        print(f"Here is ${round(total - cost, 2)} in change.")
        return True


def make_coffee(coffee):
    if is_resource_sufficient(coffee) and process_coins(coffee):
        resources['water'] -= MENU[coffee]["ingredients"]["water"]
        resources['coffee'] -= MENU[coffee]["ingredients"]["coffee"]
        resources['milk'] -= MENU[coffee]["ingredients"]["milk"]
        print(f"Here is your {coffee} ☕, Enjoy!")
    