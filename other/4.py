from collections import deque


def add_names_in_deque():
    people_data = deque()
    while True:
        name = input()
        if name == COMMAND_START:
            break
        people_data.append(name)

    return people_data


COMMAND_END = "End"
COMMAND_START = "Start"
COMMAND_REFILL = "Refill"
quantity = int(input())
people_deque = add_names_in_deque()

while True:
    command = input()

    if command == COMMAND_END:
        print(f"{quantity} liters left.")
        break

    elif command.startswith(COMMAND_REFILL):
        refill_command_date = command.split()
        refill_quantity = int(refill_command_date[1])
        quantity += refill_quantity

    else:
        person = people_deque.popleft()
        current_liters = int(command)

        if current_liters <= quantity:
            print(f"{person} gor water")
            quantity -= current_liters
        else:
            print(f"{person} must wait")