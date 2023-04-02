data = input()

while True:
    commands = input().split()

    if commands[0] == "End":
        break

    elif commands[0] == "Translate":
        char = commands[1]
        replacement = commands[2]

        data = data.replace(char, replacement)
        print(data)

    elif commands[0] == "Includes":
        substring = commands[1]
        if substring in data:
            print("True")
        else:
            print("False")

    elif commands[0] == "Start":
        substring = commands[1]

        if data.startswith(substring):
            print("True")
        else:
            print("False")
            
    elif commands[0] == "Lowercase":
        data = data.lower()
        print(data)
    elif commands[0] == "FindIndex":
        char = commands[1]
        print(data.rindex(char))
    elif commands[0] == "Remove":
        startIndex = int(commands[1])  # 2
        count = int(commands[2])  # 7

        subtring = data[startIndex:startIndex + count]
        data = data.replace(subtring, '')
        print(data)

