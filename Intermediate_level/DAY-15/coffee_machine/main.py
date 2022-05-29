from logistics import get_report, make_coffee

turn_machine_off = False

while not turn_machine_off:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        print("Turning off coffee machine...")
        turn_machine_off = True
    elif choice == "report":
        get_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        make_coffee(choice)
    else:
        print("Oops, machine crashed! Turning it off...")
        turn_machine_off = True