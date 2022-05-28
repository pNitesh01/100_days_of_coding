from math import sqrt

def check_prime(number):
    upper_val = int(sqrt(number)) + 1
    for i in range(2, upper_val):
        if number%i == 0:
            return False
    return True

n = int(input("Check this number: "))

if check_prime(number=n):
    print("It's a prime number.")
else:
    print("It's not a prime number.")
    