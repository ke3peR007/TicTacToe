# write your code here
cells = input("Enter cells:")
print("---------")
print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
print("---------")

has_empty_cells = "_" in cells or " " in cells

rows = [[cells[0], cells[3], cells[6]], [cells[1], cells[4], cells[7]], [cells[2], cells[5], cells[8]],
[cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]],
[cells[0], cells[4], cells[8]], [cells[2], cells[4], cells[6]]]

O_in_a_row = 0
X_in_a_row = 0

for row in rows:
    if row.count("X") == 3:
        X_in_a_row += 1
    elif row.count("O") == 3:
        O_in_a_row += 1

if abs(cells.count("X") - cells.count("O")) > 1:
    print("Impossible")
elif has_empty_cells and (O_in_a_row == 0 and X_in_a_row == 0):
    print("Game not finished")
elif not (has_empty_cells) and (O_in_a_row == 0 and X_in_a_row == 0):
    print("Draw")
elif X_in_a_row == 1 and O_in_a_row == 0:
    print("X wins")
elif O_in_a_row == 1 and X_in_a_row == 0:
    print("O wins")
else:
    print("Impossible")