n = int(input())
train = [0] * n  # multiplies the list elements by the command
command = input()

while command != "End":
    action = command.split()[0]  # splits into a list of strings and [0] reads 1st string in the command

    if action == "add":
        n_people = int(command.split()[1])  # [1] reads 2nd string in the command, int() turns it into a number
        train[-1] += n_people  # adds number to last integer in the list
    elif action == "insert":
        index = int(command.split()[1])
        n_people = int(command.split()[2])
        train[index] += n_people
    elif action == "leave":
        index = int(command.split()[1])
        n_people = int(command.split()[2])
        train[index] -= n_people

    command = input()

print(train)
