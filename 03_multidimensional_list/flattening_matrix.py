rows = int(input())

matrix = []
flatted = []


for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    flatted.extend(inner_list)

print(flatted)