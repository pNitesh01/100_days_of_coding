weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

bmi = weight / (height ** 2)
bmi_approx = round(bmi, 2)

print(f"Your bmi score is: {bmi_approx}")