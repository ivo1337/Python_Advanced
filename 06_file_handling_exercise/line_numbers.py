from string import punctuation


with open("files/text.txt", "r") as file:
    text = file.readlines()

output_file = open("files/output.txt", "w")

for r in range(len(text)):
    row = text[r]

    letters, marks = 0, 0

    for symbol in text[r]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {r + 1}: {''.join(text[r][:-1])} ({letters}) ({marks}) \n")

output_file.close()