import math

sequence = [int(x) for x in input().split(", ")]
low_boundary = 1
high_boundary = 10

group = math.ceil(max(sequence) / 10)

for num in range(1, group + 1):
    list_of_nums = [x for x in sequence if low_boundary <= x <= high_boundary]
    print(f"Group of {num * 10}'s: {list_of_nums}")

    low_boundary += 10
    high_boundary += 10
