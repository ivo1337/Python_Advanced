MATRIX_SIZE = 7

players = {x: 501 for x in input().split(", ")}
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(MATRIX_SIZE)]
player_one, player_two = list(players.keys())
multiplys = {"D": 2, "T": 3}


def check_valid_index(row, col):
    return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE


def multiply(row, col, letter, player):
    total_sum = 0
    for c_row in range(MATRIX_SIZE):
        if str(matrix[c_row][col]).isdigit():
            total_sum += matrix[c_row][col]
    for c_col in range(MATRIX_SIZE):
        if str(matrix[row][c_col]).isdigit():
            total_sum += matrix[row][c_col]
    players[player] -= total_sum * multiplys[letter]


counter, turn = 0, 0

while True:
    counter += 1
    hit_row, hit_col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]

    if counter % 2 != 0:
        turn += 1
        player = player_one
    else:
        player = player_two

    if check_valid_index(hit_row, hit_col):
        symbol = matrix[hit_row][hit_col]
        if str(symbol).isdigit():
            players[player] -= symbol
        elif symbol in "DT":
            multiply(hit_row, hit_col, symbol, player)
        elif symbol == "B":
            print(f"{player} won the game with {turn} throws!")
            break
        if players[player] <= 0:
            print(f"{player} won the game with {turn} throws!")
            break