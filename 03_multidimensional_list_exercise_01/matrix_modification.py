size= int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

commmand = input().split()

while commmand[0] != "END":
    type_command, row, col, value = commmand[0], int(commmand[1]), int(commmand[2]), int(commmand[3])

    if not (0 <= row < size and  0 <= col < size):
        print('Invalid coordinates')

    elif type_command == "Add":
        matrix[row][col] += value
    elif type_command == "Subtract":
        matrix[row][col] -= value

    commmand = input().split()

[print(*row) for row in matrix]