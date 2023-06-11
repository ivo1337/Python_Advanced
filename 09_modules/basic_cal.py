def sum_num(a, b):
    return a + b

def sub_num(a, b):
    return a - b

def mul_num(a, b):
    return a * b

def dev_num(a, b):
    return a / b

mapper = {
    "+": sum_num,
    "-": sub_num,
    "*": mul_num,
    "/": dev_num,
}

def execute_string(expression):
    num1, sign, num2 = expression.split()
    num1 = float(num1)
    num2 = float(num2)

    return mapper[sign](num1, num2)
