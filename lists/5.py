n = int(input())
x = []
filtered = []
for i in range(1, n+1):
    current_number = int(input())
    x.append(current_number)

command = input()
if command == "even":
    for number in x:
        if number % 2 == 0:
            filtered.append(number)
elif command == "odd":
    for number in x:
        if number % 2 != 0:
            filtered.append(number)
elif command == "negative":
    for number in x:
        if number < 0:
            filtered.append(number)
elif command == "positive":
    for number in x:
        if number >= 0:
            filtered.append(number)
print(filtered)