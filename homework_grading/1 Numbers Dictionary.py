numbers_dictionary = {}

while True:
    number_as_string = input()

    if number_as_string == "Search":
        break
    try: # check if number is int
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError: # throw error message if number is not int
         print("The variable number must be an integer")

line = input()

while line != "Remove":
    searched = line
    try: # check if searched key is present in the dictionary
        print(numbers_dictionary[searched])
    except KeyError: # throw error message if the searched key is not present in the dictionary
        print("Number does not exist in dictionary")

    line = input()

line = input()

while line != "End":
    searched = line
    try: # check if searched key is present in the dictionary
        del numbers_dictionary[searched]
    except KeyError: # throw error message if the searched key is not present in the dictionary
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)