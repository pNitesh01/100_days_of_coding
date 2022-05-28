print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_persons = int(input("How many people to split the bill? "))

total_amount = (1 + (0.01 * tip_percentage)) * total_bill
per_head_amount = round((total_amount / no_of_persons), 2)

print(f"Eachperson should pay: ${per_head_amount}")
