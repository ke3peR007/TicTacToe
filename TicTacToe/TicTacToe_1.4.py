# write your code here
cells = list(input("Enter cells:"))
# print("---------")
# print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
# print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
# print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
# print("---------")


def display():
    print("---------")
    print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
    print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
    print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
    print("---------")


def check_numbers(x, y):
    if x.isnumeric() and y.isnumeric():
        return True
    else:
        print("You should enter numbers!")
        return False


def check_coordinates(x, y):
    if int(x) >= 1 and int(x) <= 3:
        if int(y) >= 1 and int(y) <= 3:
            return True
        else:
            print("Coordinates should be from 1 to 3!")
            return False
    else:
        print("Coordinates should be from 1 to 3!")
        return False


def check_cells(x_c, y_c):
    x = int(x_c)
    y = int(y_c)
    if x == 1 and y == 1:
        if cells[6] != "_":
            return False
        else:
            return True
    if x == 1 and y == 2:
        if cells[3] != "_":
            return False
        else:
            return True
    if x == 1 and y == 3:
        if cells[0] != "_":
            return False
        else:
            return True
    if x == 2 and y == 1:
        if cells[7] != "_":
            return False
        else:
            return True
    if x == 2 and y == 2:
        if cells[4] != "_":
            return False
        else:
            return True
    if x == 2 and y == 3:
        if cells[1] != "_":
            return False
        else:
            return True
    if x == 3 and y == 1:
        if cells[8] != "_":
            return False
        else:
            return True
    if x == 3 and y == 2:
        if cells[5] != "_":
            return False
        else:
            return True
    if x == 3 and y == 3:
        if cells[2] != "_":
            return False
        else:
            return True


def fill_cell(x_c, y_c):
    x = int(x_c)
    y = int(y_c)
    if x == 1 and y == 1:
        cells[6] = "X"
    if x == 1 and y == 2:
        cells[3] = "X"
    if x == 1 and y == 3:
        cells[0] = "X"
    if x == 2 and y == 1:
        cells[7] = "X"
    if x == 2 and y == 2:
        cells[4] = "X"
    if x == 2 and y == 3:
        cells[1] = "X"
    if x == 3 and y == 1:
        cells[8] = "X"
    if x == 3 and y == 2:
        cells[5] = "X"
    if x == 3 and y == 3:
        cells[2] = "X"


display()
while True:
    user_input = input("enter coordinates: ").split()
    # print(user_input)
    if len(user_input) > 1:
        x_axis = user_input[0]
        y_axis = user_input[1]
        # print(user_input)
        if check_numbers(x_axis, y_axis):
            # print(check_numbers(x_axis, y_axis))
            if check_coordinates(x_axis, y_axis):
                # print(check_coordinates(x_axis, y_axis))
                if check_cells(x_axis, y_axis):
                    print(check_cells(x_axis, y_axis))
                    fill_cell(x_axis, y_axis)
                    display()
                    break
                else:
                    print("This cell is occupied! Choose another one!")
    else:
        print("You should enter numbers!")



# has_empty_cells = "_" in cells or " " in cells
#
# rows = [[cells[0], cells[3], cells[6]], [cells[1], cells[4], cells[7]], [cells[2], cells[5], cells[8]],
# [cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]],
# [cells[0], cells[4], cells[8]], [cells[2], cells[4], cells[6]]]

# O_in_a_row = 0
# X_in_a_row = 0
#
# for row in rows:
#     if row.count("X") == 3:
#         X_in_a_row += 1
#     elif row.count("O") == 3:
#         O_in_a_row += 1
#
# if abs(cells.count("X") - cells.count("O")) > 1:
#     print("Impossible")
# elif has_empty_cells and (O_in_a_row == 0 and X_in_a_row == 0):
#     print("Game not finished")
# elif not (has_empty_cells) and (O_in_a_row == 0 and X_in_a_row == 0):
#     print("Draw")
# elif X_in_a_row == 1 and O_in_a_row == 0:
#     print("X wins")
# elif O_in_a_row == 1 and X_in_a_row == 0:
#     print("O wins")
# else:
#     print("Impossible")
