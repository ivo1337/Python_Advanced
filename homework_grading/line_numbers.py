from string import punctuation

with open("text.txt", "r") as file:
    text = file.readlines()

output_file = open("output.txt", "w")

for i in range(0, len(text)):
    row = text[i]
    letter_counter = 0
    symbols_counter = 0

    for symbol in row:
        if symbol.isalpha():
            letter_counter += 1
        elif symbol in punctuation:
            symbols_counter += 1

    output_file.write(f"Line:{i+1} {''.join(row[:-1])} ({letter_counter})({symbols_counter})\n")

output_file.close()
