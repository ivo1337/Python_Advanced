stack_parant = []

text = input()

for index in range(len(text)):
    if text[index] == "(":
        stack_parant.append(index)
    elif text[index] == ")":
        start = stack_parant.pop()
        end = index + 1
        print(text[start:end])
