rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for row in range(rows)]


equal_blocks = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        symbols = matrix[row][col]

        if matrix[row][col + 1] == symbols and  matrix[row + 1][col] == symbols and matrix[row + 1][col + 1] == symbols:
            equal_blocks += 1

print(equal_blocks)