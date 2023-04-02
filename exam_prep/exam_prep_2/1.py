encrypted_message = input()

while True:
    command = input().split("|")

    if command[0] == "Decode":
        break

    elif command[0] == "Move":
        number_of_letters = int(command[1])
        first_half = encrypted_message[:number_of_letters]
        second_half = encrypted_message[number_of_letters:]

        encrypted_message = second_half + first_half

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]

        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]

        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")


