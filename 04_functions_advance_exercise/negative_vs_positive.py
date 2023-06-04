def print_numbers(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
positive_num = sum(x for x in numbers if x > 0)
negative_num = sum(x for x in numbers if x < 0)

print_numbers(positive_num, negative_num)