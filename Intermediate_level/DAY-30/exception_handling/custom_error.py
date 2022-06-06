height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height must not be greater than 3m.")

bmi = weight / height ** 2
print(bmi)