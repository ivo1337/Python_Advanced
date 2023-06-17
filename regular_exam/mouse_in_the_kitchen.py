def mouse_cheese_hunt():
    dimensions = input().split(',')
    rows, cols = int(dimensions[0]), int(dimensions[1])

    matrix = []
    mouse_position = None
    cheese_count = 0

    for _ in range(rows):
        row = list(input())
        matrix.append(row)
        if 'M' in row:
            mouse_position = (matrix.index(row), row.index('M'))
        cheese_count += row.count('C')

    directions = []
    while True:
        command = input()
        if command == 'danger':
            break
        directions.append(command)

    def is_valid_position(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def update_position(row, col, symbol):
        matrix[row][col] = symbol

    def print_matrix():
        for row in matrix:
            print(''.join(row))

    def end_game(message):
        print(message)
        print_matrix()
        return

    for direction in directions:
        current_row, current_col = mouse_position
        new_row, new_col = current_row, current_col

        if direction == 'up':
            new_row -= 1
        elif direction == 'down':
            new_row += 1
        elif direction == 'left':
            new_col -= 1
        elif direction == 'right':
            new_col += 1

        if not is_valid_position(new_row, new_col):
            end_game("No more cheese for tonight!")
            return

        target = matrix[new_row][new_col]

        if target == '@':
            continue
        elif target == 'C':
            cheese_count -= 1
            if cheese_count == 0:
                update_position(current_row, current_col, '*')
                update_position(new_row, new_col, 'M')
                end_game("Happy mouse! All the cheese is eaten, good night!")
                return
            else:
                update_position(current_row, current_col, '*')
                update_position(new_row, new_col, 'M')
        elif target == 'T':
            update_position(current_row, current_col, '*')
            update_position(new_row, new_col, 'M')
            end_game("Mouse is trapped!")
            return
        elif target == '*':
            update_position(current_row, current_col, '*')
            update_position(new_row, new_col, 'M')

        mouse_position = (new_row, new_col)

    end_game("Mouse will come back later!")


mouse_cheese_hunt()
