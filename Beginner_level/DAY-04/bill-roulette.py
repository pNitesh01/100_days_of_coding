import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

index = random.randint(0, len(names)-1)
print(f"{names[index]} has to buy the meal today!")

print(f"{random.choice(names)} has to buy the meal today!")
