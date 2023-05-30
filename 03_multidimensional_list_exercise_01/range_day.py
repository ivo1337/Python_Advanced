def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)
    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position
    if field[r][c] == "x":
        return my_position

    return [r, c]
def shoot(direction):
    r = my_position[0] + direction[direction][0]
    c = my_position[1] + direction[direction][1]
    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position
    if field[r][c] == "x":
        return my_position

    return [r, c]

SIZE = 5

field = []

targets = 0
targets_hit = 0
targets_hit_positions = []

my_position = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0,-1),
    'right': (0, 1),
}

for row in range(SIZE):
    field.append(input().split())

    if 'A' in field[row]:
        my_position=[row, field[row].index('A')]

    targets += field[row].count('x')

for _ in range(int(input())):
    command = input.split()

    if command[0] == "move":
        my_position = move(command[1], int(command[2]))
    elif command[0] == 'shoot':
        pass
