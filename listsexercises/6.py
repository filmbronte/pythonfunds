numbers = [int(x) for x in input().split()]
n = int(input())

for _ in range(n):
    min_number = min(numbers)
    numbers.remove(min_number)

print(', '.join([str(x) for x in numbers]))

