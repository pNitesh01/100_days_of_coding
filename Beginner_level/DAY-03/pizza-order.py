print("Welcome to Python Pizza Deliveries!")
size = str.lower(input("What size pizza do you want? S, M, L: "))
add_pepperoni = str.lower(input("Do you want pepperoni? Y or N: "))
extra_cheese = str.lower(input("Do you want extra cheese? Y or N: "))

bill_amount = 0

if size == 's':
    bill_amount = 15
    
    if add_pepperoni == 'y':
        bill_amount += 2
        
elif size == 'm':
    bill_amount = 20
    
    if add_pepperoni == 'y':
        bill_amount += 3
        
else:
    bill_amount = 25
    
    if add_pepperoni == 'y':
        bill_amount += 3
        
if extra_cheese == 'y':
    bill_amount += 1
    
print(f"Your final bill is: ${bill_amount}.")