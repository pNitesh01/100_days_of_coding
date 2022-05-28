from math import ceil

def cal_no_of_cans(height, weight, cover):
    area = height * weight
    no_of_cans = area / cover
    return ceil(no_of_cans)

test_h = int(input("Height of wall: "))
test_w = int(input("Weight of wall: "))
coverage = 5

no_of_cans_reqd = cal_no_of_cans(height=test_h, weight=test_w, cover=coverage)

print(f"You'll need {no_of_cans_reqd} cans of paint.")