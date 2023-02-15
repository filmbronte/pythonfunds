names = input().split(", ")

sorted_names = sorted(names, key=lambda x: (-len(x), x))  # len() sorts them by length and x sorts them alphabetically
print(sorted_names)
