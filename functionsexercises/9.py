def is_valid_length(password):
    return 10 >= len(password) >= 6


def is_letters_and_digits(password):
    return password.isalnum()


def is_more_than_2_num(password):
    counter = 0
    for ch in password:
        if ch.isdigit():
            counter += 1

    return counter >= 2


password = input()
isValid = True

if not is_valid_length(password):
    isValid = False
    print("Password must be between 6 and 10 characters")

if not is_letters_and_digits(password):
    isValid = False
    print("Password must consist only of letters and digits")

if not is_more_than_2_num(password):
    isValid = False
    print("Password must have at least 2 digits")

if isValid:
    print("Password is valid")
