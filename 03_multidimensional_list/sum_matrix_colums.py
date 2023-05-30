rows, columns = map(int, input().split(', '))

matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for j in range(columns):
    column_sum = sum(row[j] for row in matrix)
    print(column_sum)