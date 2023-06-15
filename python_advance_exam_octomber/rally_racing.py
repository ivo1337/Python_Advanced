matrix_size = int(input())
cars_number = input()

directions = {
    "up": lambda r, c: [(r - 1) % matrix_size, c],
    "down": lambda r, c: [(r + 1) % matrix_size, c],
    "left": lambda r, c: [r, (c - 1) % matrix_size],
    "right": lambda r, c: [r, (c + 1) % matrix_size],
}

matrix = []
