cards = input().split()
n = int(input())

for _ in range(n):
    first_half = []
    second_half = []

    for i in range(1, len(cards) - 1):
        if i < len(cards) / 2:
            first_half.append(cards[i])
        else:
            second_half.append(cards[i])

    shuffled = []
    first_part_index = 0
    second_part_index = 0
    for i in range(len(first_half) * 2):
        if i % 2 == 0:
            shuffled.append(second_half[second_part_index])
            second_part_index += 1
        else:
            shuffled.append(first_half[first_part_index])
            first_part_index += 1

    cards = [cards[0]] + shuffled + [cards[-1]]

print(cards)


