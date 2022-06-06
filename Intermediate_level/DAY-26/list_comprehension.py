numbers = [1, 2, 3]

# Without list comprehension
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)    
print(new_list)
    
# With list comprehension
new_list2 = [n + 1 for n in numbers]
print(new_list2)

# NOTE: list comprehension applicable to-
#     1. list
#     2. range
#     3. string
#     4. tuple

# Conditional list comprehension
new_list3 = [x*2 for x in range(1,10) if x%2 == 0]
print(new_list3)