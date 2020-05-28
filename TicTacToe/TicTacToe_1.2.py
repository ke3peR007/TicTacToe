user_input = input("Enter Cells: ")

print("---------")
print("| " + user_input[0] + " " + user_input[1] + " " + user_input[2] + " |")
print("| " + user_input[3] + " " + user_input[4] + " " + user_input[5] + " |")
print("| " + user_input[6] + " " + user_input[7] + " " + user_input[8] + " |")
print("---------")

user_list = [x for x in user_input]
print(user_list)
x_count = 0
o_count = 0
# y = 0
for y in user_list:
    if y == "X":
        x_count += 1
    if y == "O":
        o_count += 1
print(x_count)
print(o_count)
matrix = []
k = 0
for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(user_input[k])
        k += 1
        # print(matrix[i])
print(matrix)
if (("X" == matrix[0][0] == matrix[0][1] == matrix[0][2]
       or "X" == matrix[1][0] == matrix[1][1] == matrix[1][2]
       or "X" == matrix[2][0] == matrix[2][1] == matrix[2][2]
       or "X" == matrix[0][0] == matrix[1][0] == matrix[2][0]
       or "X" == matrix[0][1] == matrix[1][1] == matrix[2][1]
       or "X" == matrix[0][2] == matrix[1][2] == matrix[2][2]
       or "X" == matrix[0][0] == matrix[1][1] == matrix[2][2]
       or "X" == matrix[0][2] == matrix[1][1] == matrix[2][0]) \
        and ("O" == matrix[0][0] == matrix[0][1] == matrix[0][2]
             or "O" == matrix[1][0] == matrix[1][1] == matrix[1][2]
             or "O" == matrix[2][0] == matrix[2][1] == matrix[2][2]
             or "O" == matrix[0][0] == matrix[1][0] == matrix[2][0]
             or "O" == matrix[0][1] == matrix[1][1] == matrix[2][1]
             or "O" == matrix[0][2] == matrix[1][2] == matrix[2][2]
             or "O" == matrix[0][0] == matrix[1][1] == matrix[2][2]
             or "O" == matrix[0][2] == matrix[1][1] == matrix[2][0])) \
        or (x_count - o_count >=2 or o_count - x_count >= 2):
    print("Impossible")
elif ("X" == matrix[0][0] == matrix[0][1] == matrix[0][2]
        or "X" == matrix[1][0] == matrix[1][1] == matrix[1][2]
        or "X" == matrix[2][0] == matrix[2][1] == matrix[2][2]
        or "X" == matrix[0][0] == matrix[1][0] == matrix[2][0]
        or "X" == matrix[0][1] == matrix[1][1] == matrix[2][1]
        or "X" == matrix[0][2] == matrix[1][2] == matrix[2][2]
        or "X" == matrix[0][0] == matrix[1][1] == matrix[2][2]
        or "X" == matrix[0][2] == matrix[1][1] == matrix[2][0]):
    # if "X" == matrix[0][0]:
    print("X wins")
elif "O" == matrix[0][0] == matrix[0][1] == matrix[0][2] \
        or "O" == matrix[1][0] == matrix[1][1] == matrix[1][2] \
        or "O" == matrix[2][0] == matrix[2][1] == matrix[2][2]\
        or "O" == matrix[0][0] == matrix[1][0] == matrix[2][0] \
        or "O" == matrix[0][1] == matrix[1][1] == matrix[2][1] \
        or "O" == matrix[0][2] == matrix[1][2] == matrix[2][2]\
        or "O" == matrix[0][0] == matrix[1][1] == matrix[2][2]\
        or "O" == matrix[0][2] == matrix[1][1] == matrix[2][0]:
    # if "X" == matrix[0][0]:
    print("O wins")
# elif ((matrix[0][0] != matrix[0][1] != matrix[0][2] != "_"
#        or matrix[1][0] != matrix[1][1] != matrix[1][2] != "_"
#        or matrix[2][0] != matrix[2][1] != matrix[2][2] != "_")
#       and (matrix[0][0] != matrix[1][0] != matrix[2][0] != "_"
#            or matrix[0][1] != matrix[1][1] != matrix[2][1] != "_"
#            or matrix[0][2] != matrix[1][2] != matrix[2][2] != "_")
#       and (matrix[0][0] != matrix[1][1] != matrix[2][2] != "_"
#            or matrix[0][2] != matrix[1][1] != matrix[2][0]) != "_") and (x_count == o_count):
elif x_count - o_count == 1:
    print("Draw")
elif (("X" == matrix[0][0] == matrix[0][1] == matrix[0][2]
       or "X" == matrix[1][0] == matrix[1][1] == matrix[1][2]
       or "X" == matrix[2][0] == matrix[2][1] == matrix[2][2]
       or "X" == matrix[0][0] == matrix[1][0] == matrix[2][0]
       or "X" == matrix[0][1] == matrix[1][1] == matrix[2][1]
       or "X" == matrix[0][2] == matrix[1][2] == matrix[2][2]
       or "X" == matrix[0][0] == matrix[1][1] == matrix[2][2]
       or "X" == matrix[0][2] == matrix[1][1] == matrix[2][0])
        and ("O" == matrix[0][0] == matrix[0][1] == matrix[0][2]
             or "O" == matrix[1][0] == matrix[1][1] == matrix[1][2]
             or "O" == matrix[2][0] == matrix[2][1] == matrix[2][2]
             or "O" == matrix[0][0] == matrix[1][0] == matrix[2][0]
             or "O" == matrix[0][1] == matrix[1][1] == matrix[2][1]
             or "O" == matrix[0][2] == matrix[1][2] == matrix[2][2]
             or "O" == matrix[0][0] == matrix[1][1] == matrix[2][2]
             or "O" == matrix[0][2] == matrix[1][1] == matrix[2][0])) \
        or ((x_count > o_count) and (x_count != 0 or x_count != 1)) or ((o_count > x_count) and (o_count != 0 or o_count != 1)):
    print("impossible")
else:
    print("Game not finished")
# elif matrix[0][0] == matrix[1][0] == matrix[2][0] \
#         or matrix[0][1] == matrix[1][1] == matrix[2][1] \
#         or matrix[0][2] == matrix[1][2] == matrix[2][2]:
#     print("x wins")

# if (("X" == matrix[0][0] == matrix[0][1] == matrix[0][2]
#        or "X" == matrix[1][0] == matrix[1][1] == matrix[1][2]
#        or "X" == matrix[2][0] == matrix[2][1] == matrix[2][2]
#        or "X" == matrix[0][0] == matrix[1][0] == matrix[2][0]
#        or "X" == matrix[0][1] == matrix[1][1] == matrix[2][1]
#        or "X" == matrix[0][2] == matrix[1][2] == matrix[2][2]
#        or "X" == matrix[0][0] == matrix[1][1] == matrix[2][2]
#        or "X" == matrix[0][2] == matrix[1][1] == matrix[2][0]) \
#         and ("O" == matrix[0][0] == matrix[0][1] == matrix[0][2]
#              or "O" == matrix[1][0] == matrix[1][1] == matrix[1][2]
#              or "O" == matrix[2][0] == matrix[2][1] == matrix[2][2]
#              or "O" == matrix[0][0] == matrix[1][0] == matrix[2][0]
#              or "O" == matrix[0][1] == matrix[1][1] == matrix[2][1]
#              or "O" == matrix[0][2] == matrix[1][2] == matrix[2][2]
#              or "O" == matrix[0][0] == matrix[1][1] == matrix[2][2]
#              or "O" == matrix[0][2] == matrix[1][1] == matrix[2][0])) \
#         or ((x_count > o_count) and ((x_count - o_count) != 1 or (x_count - o_count) != 0)) \
#         or ((o_count > x_count) and ((o_count - x_count) != 1 or (o_count - x_count) != 0)):
#     print("impossible")
