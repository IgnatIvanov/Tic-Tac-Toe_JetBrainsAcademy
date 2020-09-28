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

def convert_coordinates(x, y):
    if x == 1 and y == 3:
        return "2 2"
    if x == 2 and y == 3:
        return "2 1"
    if x == 3 and y == 3:
        return "2 0"
    if x == 1 and y == 2:
        return "1 2"
    if x == 2 and y == 2:
        return "1 1"
    if x == 3 and y == 2:
        return "1 0"
    if x == 1 and y == 1:
        return "0 2"
    if x == 2 and y == 1:
        return "0 1"
    if x == 3 and y == 1:
        return "0 0"

def check(in_coord):
    if len(in_coord) != 2:
        return True

    if len(in_coord[0]) != 1 or len(in_coord[1]) != 1:
        return True

    if in_coord[0] not in digits or in_coord[1] not in digits:
        return True

    return False

digits = "0123456789"

u_input = input("Enter cells: ")
cells = [[u_input[8], u_input[7], u_input[6]],
         [u_input[5], u_input[4], u_input[3]],
         [u_input[2], u_input[1], u_input[0]]]

print("---------")
print("|", cells[2][2], cells[2][1], cells[2][0], "|")
print("|", cells[1][2], cells[1][1], cells[1][0], "|")
print("|", cells[0][2], cells[0][1], cells[0][0], "|")
print("---------")

while True:
    coordinates = input("Enter the coordinates: ").split(" ")
    if check(coordinates):
        print("You should enter numbers!")
        continue
    elif int(coordinates[0]) > 3 or int(coordinates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    elif int(coordinates[0]) < 1 or int(coordinates[1]) < 1:
        print("Coordinates should be from 1 to 3!")
        continue

    coordinates = convert_coordinates(int(coordinates[0]), int(coordinates[1])).split(" ")

    if cells[int(coordinates[0])][int(coordinates[1])] != "_":
        print("This cell is occupied! Choose another one!")
    else:
        cells[int(coordinates[0])][int(coordinates[1])] = "X"
        break

print("---------")
print("|", cells[2][2], cells[2][1], cells[2][0], "|")
print("|", cells[1][2], cells[1][1], cells[1][0], "|")
print("|", cells[0][2], cells[0][1], cells[0][0], "|")
print("---------")

#if abs(u_input.count("X") - u_input.count("O")) > 1 or is_wins("X") and is_wins("O"):
#    print("Impossible")
#elif is_wins("X"):
#    print("X wins")
#elif is_wins("O"):
#    print("O wins")
#elif u_input.count("_") == 0:
#    print("Draw")
#else:
#    print("Game not finished")