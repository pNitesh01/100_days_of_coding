current_age = int(input("What is your current age? "))
years_left = 90 - current_age

months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
