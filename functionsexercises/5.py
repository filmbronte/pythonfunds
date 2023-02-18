numbers = input().split()
lst = []


def is_even(x):
    return x % 2 == 0


for num in numbers:
    lst.append(int(num))

print(list(filter(is_even, lst)))
