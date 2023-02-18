n1 = int(input())
n2 = int(input())
n3 = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    sum_result = sum_numbers(n1, n2)
    result = subtract(sum_result, n3)

    return result


print(add_and_subtract(n1, n2, n3))






