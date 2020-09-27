def is_wins(player):
    for i in range(0, 3):
        if cells[0][i] == player and cells[1][i] == player and cells[2][i] == player:
            return True
    for i in range(0, 3):
        if cells[i][0] == player and cells[i][1] == player and cells[i][2] == player:
            return True
    if cells[0][0] == player and cells[1][1] == player and cells[2][2] == player:
        return True
    if cells[0][2] == player and cells[1][1] == player and cells[2][0] == player:
        return True

u_input = input("Enter cells: ")
cells = [[u_input[0], u_input[1], u_input[2]],
         [u_input[3], u_input[4], u_input[5]],
         [u_input[6], u_input[7], u_input[8]]]

print("---------")
print("|", cells[0][0], cells[0][1], cells[0][2], "|")
print("|", cells[1][0], cells[1][1], cells[1][2], "|")
print("|", cells[2][0], cells[2][1], cells[2][2], "|")
print("---------")

if abs(u_input.count("X") - u_input.count("O")) > 1 or is_wins("X") and is_wins("O"):
    print("Impossible")
elif is_wins("X"):
    print("X wins")
elif is_wins("O"):
    print("O wins")
elif u_input.count("_") == 0:
    print("Draw")
else:
    print("Game not finished")