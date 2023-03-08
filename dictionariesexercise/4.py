# data = input()
# n = int(input())
# phone_dict = {}
#
# for _ in range(n):
#     for el in data:
#         name, number = data.split("-")
#         number = int(number)
#         if el not in phone_dict:
#             phone_dict[name] = number
#         else:
#             phone_dict[name] += number
#
#     data = input()
#
#     for key, value in phone_dict.items():
#         if data not in phone_dict:
#             print(f"Contact {key} does not exist.")
#         else:
#             print(f"{key} -> {value}")
#
#
def phone_book_information(number_of_lines, phone_book):
    for x in range(number_of_lines):
        name = input()
        if name not in phone_book:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phone_book[name]}")

    return True


def phone_book_info():
    phone_book = {}
    condition = False

    while True:
        contact_information = input().split("-")

        if contact_information[0].isdigit():
            condition = phone_book_information(int(contact_information[0]), phone_book)
        else:
            phone_book[contact_information[0]] = contact_information[1]

        if condition:
            break


phone_book_info()
