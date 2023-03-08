# data = input()
# d = {}
#
# for ch in data:
#     if ch not in d and ch != " ":
#         d[ch] = 1
#     elif ch in d and ch != " ":
#         d[ch] += 1
#
# # {char} -> {occurrences}
# for key, value in d.items():
#     print(f"{key} -> {value}")

from collections import Counter

word = input()
result = Counter(word)

for key, value in result.items():
    if key != " ":
        print(f"{key} -> {value}")

