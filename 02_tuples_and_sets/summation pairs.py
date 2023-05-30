numbers = list(map(int, input().split()))
target = int(input())

found_pairs = set()

for i, num1 in enumerate(numbers):
    for j, num2 in enumerate(numbers):
        if i != j and num1 + num2 == target:
            found_pairs.add(tuple(sorted([num1, num2])))

for pair in found_pairs:
    print(f"{pair[0]} + {pair[1]} = {target}")
