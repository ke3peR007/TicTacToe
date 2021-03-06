def display_board(cells):
    print("---------")
    print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
    print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
    print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
    print("---------")
    pass


def check_board(cells, counter):
    rows = [[cells[0], cells[3], cells[6]], [cells[1], cells[4], cells[7]], [cells[2], cells[5], cells[8]],
            [cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]],
            [cells[0], cells[4], cells[8]], [cells[2], cells[4], cells[6]]]

    O_in_a_row = 0
    X_in_a_row = 0
    counter += 1
    for row in rows:
        if row.count("X") == 3:
            X_in_a_row += 1
        elif row.count("O") == 3:
            O_in_a_row += 1

    if abs(cells.count("X") - cells.count("O")) > 1:
        print("Impossible")
        return "Impossible"
    elif has_empty_cells and (O_in_a_row == 0 and X_in_a_row == 0):
        print("Game not finished")
        return "Game not finished"
    elif not (has_empty_cells) and (O_in_a_row == 0 and X_in_a_row == 0):
        print("Draw")
        return "Draw"
    elif X_in_a_row == 1 and O_in_a_row == 0:
        print("X wins")
        return "X wins"
    elif O_in_a_row == 1 and X_in_a_row == 0:
        print("O wins")
        return "O wins"
    else:
        print("Impossible")
        return "Impossible"


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


def check_cells(x_c, y_c, cells):
    x = int(x_c)
    y = int(y_c)
    if x == 1 and y == 1:
        if cells[6] != " ":
            return False
        else:
            return True
    if x == 1 and y == 2:
        if cells[3] != " ":
            return False
        else:
            return True
    if x == 1 and y == 3:
        if cells[0] != " ":
            return False
        else:
            return True
    if x == 2 and y == 1:
        if cells[7] != " ":
            return False
        else:
            return True
    if x == 2 and y == 2:
        if cells[4] != " ":
            return False
        else:
            return True
    if x == 2 and y == 3:
        if cells[1] != " ":
            return False
        else:
            return True
    if x == 3 and y == 1:
        if cells[8] != " ":
            return False
        else:
            return True
    if x == 3 and y == 2:
        if cells[5] != " ":
            return False
        else:
            return True
    if x == 3 and y == 3:
        if cells[2] != " ":
            return False
        else:
            return True


def fill_cell(x_c, y_c, cells, player):
    x = int(x_c)
    y = int(y_c)
    if x == 1 and y == 1:
        cells[6] = player
    if x == 1 and y == 2:
        cells[3] = player
    if x == 1 and y == 3:
        cells[0] = player
    if x == 2 and y == 1:
        cells[7] = player
    if x == 2 and y == 2:
        cells[4] = player
    if x == 2 and y == 3:
        cells[1] = player
    if x == 3 and y == 1:
        cells[8] = player
    if x == 3 and y == 2:
        cells[5] = player
    if x == 3 and y == 3:
        cells[2] = player


def take_input(cells,c):
    turn = "X"
    while True:
        if c < 9:
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
                        if check_cells(x_axis, y_axis, cells):
                            print(check_cells(x_axis, y_axis, cells))
                            print(turn)
                            # display_board(cells)
                            if turn == "X":
                                fill_cell(x_axis, y_axis, cells, turn)
                                turn = "O"
                                display_board(cells)
                                if c < 9:
                                    if check_board(board,c) == "Game not finished" and c != 9:
                                        continue
                                    elif check_board(board,c) == "Impossible":
                                        break
                                    elif check_board(board,c) == "X wins":
                                        break
                                else:
                                    break
                            else:
                                fill_cell(x_axis, y_axis, cells, turn)
                                turn = "X"
                                display_board(cells)
                                print(c)
                                if c < 9:
                                    if check_board(board, c) == "Game not finished" and c != 9:
                                        continue
                                    if check_board(board, c) == "Impossible":
                                        break
                                    if check_board(board, c) == "O wins":
                                        break
                                else:
                                    break
                        else:
                            print("This cell is occupied! Choose another one!")
            else:
                print("You should enter numbers!")
        else:
            break

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
has_empty_cells = "_" in board or " " in board
count = 0
display_board(board)
# while True:
take_input(board, count)
    # print("here")
    # if take_input(board) == "X wins":
    #     print("x wins in outer loop")
    #     break
# print("enter coordinates: ")
