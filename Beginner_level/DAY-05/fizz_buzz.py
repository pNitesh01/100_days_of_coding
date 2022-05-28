list_of_numbers = []

for x in range(1, 101):
    if x%15 == 0:
        list_of_numbers.append("FizzBuzz")
    elif x%5 == 0:
        list_of_numbers.append("Buzz")
    elif x%3 == 0:
        list_of_numbers.append("Fizz")
    else:
        list_of_numbers.append(x)
        
print(list_of_numbers)