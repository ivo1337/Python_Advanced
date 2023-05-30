
size = int(input())
matrix = [list(input())for  _ in range(size)]
position = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2),
)

removed_knights = 0

while  True:
    max_attacks = 0
    knights_most_att = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in position:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == 'K':
                            attacks += 1
                    if attacks > max_attacks:
                        knights_most_att = [row, col]
                        max_attacks = attacks

    if knights_most_att:
        matrix[knights_most_att[0]][knights_most_att[1]] = "0"
        removed_knights += 1

    else:
        break
print(removed_knights)