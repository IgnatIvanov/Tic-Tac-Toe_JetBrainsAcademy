height = int(input())
current_floor = "#"
for i in range(0, height):
    foundation = height * 2 - 1
    print(current_floor.center(foundation))
    current_floor += "##"