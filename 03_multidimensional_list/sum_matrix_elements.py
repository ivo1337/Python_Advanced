rows, cols = [int(el) for el in input().split(", ")]
matrix = []
sum_nums = 0
for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)
    sum_nums += sum(inner_list)

# sum_nums = 0
# for row_index in range(rows):
#     for col_index in range(cols):
#         sum_nums += matrix[row_index][col_index]


print(sum_nums)
print(matrix)