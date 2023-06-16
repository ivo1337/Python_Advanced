SIZE = 6
matrix = [[x if x.isalpha() else int(x) for x in input().split()] for _ in range(SIZE)]
total_sum = 0

for trow in range(3):
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    try:
        symbol = matrix[row][col]
    except IndexError:
        continue

    if symbol == "B":
        matrix[row][col] = 0
        for c_row in range(SIZE):
            total_sum += matrix[c_row][col]

if total_sum < 100:
    print(f"Sorry! You need {100-total_sum} points more to win a prize.")

else:
    if total_sum < 200:
        toy = "Football"
    elif total_sum < 300:
        toy = "Teddy Bear"
    elif total_sum >= 300:
        toy = "Lego Construction Set"
    print(f"Good job! You scored {total_sum} points, and you've won {toy}.")
