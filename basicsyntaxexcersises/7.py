while True:
    word = input()

    if word == "End":
        break
    if word == "SoftUni":
        continue

    line = ''
    for ch in word:
        line += ch * 2

    print(line)
