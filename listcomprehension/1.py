text = input()
lst = [char for char in text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

# for char in text:
#     if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         lst.append(char)


print("".join(lst))  # prints list as a string

