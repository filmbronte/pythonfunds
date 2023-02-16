n = int(input())
capacity = 255
total = 0

for i in range(n):
    liters = int(input())

    if liters + total > capacity:
        print("Insufficient capacity!")
        continue
    else:
        total += liters

print(total)

