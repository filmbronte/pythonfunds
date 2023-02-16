n = int(input())

total_sum = 0
for x in range(n):
    letter = input()

    for char in letter:
        value = ord(char)
        total_sum += value

print(f"The sum equals: {total_sum}")
