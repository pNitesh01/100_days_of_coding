row1 = ["O","O","O"]
row2 = ["O","O","O"]
row3 = ["O","O","O"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
row_index = int(position[0]) - 1
col_index = int(position[1]) - 1

map[row_index][col_index] = "X"

print(f"{row1}\n{row2}\n{row3}")