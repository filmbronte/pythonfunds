calculation_type = input()
first_number = int(input())
second_number = int(input())


# # "multiply", "divide", "add", "subtract".
#
# def calculate():
#     if calculation_type == "multiply":
#         print(first_number * second_number)
#     elif calculation_type == "divide":
#         print(first_number / second_number)
#     elif calculation_type == "add":
#         print(first_number + second_number)
#     elif calculation_type == "subtract":
#         print(first_number - second_number)
#
#
# calculate()

def calculate(a, b, result):
    result = None
    if calculation_type == "multiply":
        result = a * b
    elif calculation_type == "divide":
        result = int(a / b)
    elif calculation_type == "add":
        result = a + b
    elif calculation_type == "subtract":
        result = a - b
    return result


res = calculate(first_number, second_number, calculation_type)
print(res)
