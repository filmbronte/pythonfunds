n = int(input())

for i in range(n):
    word = input()
    isPure = True

    for ch in word:
        if ch == "," or ch == "." or ch == "_":
            isPure = False
            break

    if isPure:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")
