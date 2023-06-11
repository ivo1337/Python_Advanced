import os

while True:
    command, *info = input().split("-")
    if command == "End":
        break

    file_name = info[0]

    if command == "Create":
        with open(f"{file_name}", "w"):
            pass

    elif command == "Add":
        content = info[1]
        with open(f"{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        old_string = info[1]
        new_string = info[2]
        try:
            with open(f"{file_name}", "r+") as file:
                text = file.read()
                text = text.replace(old_string, new_string)
                file.seek(0)
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"{file_name}")

        except FileNotFoundError:
            print("An error occurred")
