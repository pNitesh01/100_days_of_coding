from kitchen import MENU, resources

money_left = 0

def get_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money_left}")

def is_resource_sufficient(coffee):
    if coffee == 'espresso':
        if resources['water'] < MENU["espresso"]['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU["espresso"]['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            return True
        return False
    
    elif coffee == 'latte':
        if resources['water'] < MENU["latte"]['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU["latte"]['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        elif resources['milk'] < MENU["latte"]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
        else:
            return True
        return False
        
    else:
        if resources['water'] < MENU["cappuccino"]['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU["cappuccino"]['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        elif resources['milk'] < MENU["cappuccino"]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
        else:
            return True
        return False

def process_coins(coffee):
    global money_left
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_amount_given = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
    
    if coffee == 'espresso' and total_amount_given >= MENU["espresso"]['cost']:
        money_left += MENU["espresso"]['cost']
        print(f"Here is ${round(total_amount_given - MENU['espresso']['cost'], 2)} in change.")
    
    elif coffee == 'latte' and total_amount_given >= MENU["latte"]['cost']:
        money_left += MENU["latte"]['cost']
        print(f"Here is ${round(total_amount_given - MENU['latte']['cost'], 2)} in change.")
    
    elif coffee == 'cappuccino' and total_amount_given >= MENU["cappuccino"]['cost']:
        money_left += MENU["cappuccino"]['cost']
        print(f"Here is ${round(total_amount_given - MENU['cappuccino']['cost'], 2)} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True

def make_coffee(coffee):
    if coffee == 'espresso' and is_resource_sufficient('espresso'):
        if process_coins('espresso'):
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print("Here is your Espresso ☕, Enjoy!")
            
    elif coffee == 'latte' and is_resource_sufficient('latte'):
        if process_coins('latte'):
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            print("Here is your Latte ☕, Enjoy!")
            
    elif coffee == 'cappuccino' and is_resource_sufficient('cappuccino'):
        if process_coins('cappuccino'):
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            print("Here is your Cappuccino ☕, Enjoy!")
