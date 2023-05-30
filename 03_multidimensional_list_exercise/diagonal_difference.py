n = int(input())
matrix  = [[int(n) for n in input().split()] for row in range(n)]

primary_sum = 0
secondary_sum = 0

for i in range(n):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][n - i - 1]

print(abs(primary_sum - secondary_sum))