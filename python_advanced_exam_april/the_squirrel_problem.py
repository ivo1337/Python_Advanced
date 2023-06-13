size = int(input())

deposit = {"h": ["Hazelnut", 0], "t": ["Trap", 0]}
directions = {
    "up": lambda r, c: [(r - 1) % size, c],
    "down": lambda r, c: [(r + 1) % size, c],
    "left": lambda r, c: [r, (c - 1) % size],
    "right": lambda r, c: [r, (c + 1) % size],
}
matrix = []
squirrel_pos = []
hazelnuts = 0

commands = input().split(", ")

for row in range(size):
    current_row = input().split("*")

    if "s" in current_row:
        squirrel_pos = [row, current_row.index("s")]
    if "h" in current_row:
        hazelnuts += current_row.count("h")

    matrix.append(current_row)

for command in commands:
    squirrel_pos = directions[command](*squirrel_pos)
    position = matrix[squirrel_pos[0]][squirrel_pos[1]]

    if position in deposit:
        deposit[position][1] += 1

    elif position == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    # Check if the squirrel is out of the field
    if squirrel_pos[0] < 0 or squirrel_pos[0] >= size or squirrel_pos[1] < 0 or squirrel_pos[1] >= size:
        print("The squirrel went out of the field.")
        break

else:
    print(f"Hazelnuts collected: {deposit['h'][1]}")