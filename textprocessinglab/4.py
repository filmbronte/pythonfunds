# ch = "a"
# new = ord(ch) + 3
# print(new)

text = input()
encrypted_text = []

for ch in text:
    new = ord(ch) + 3
    encrypted_text.append(chr(new))

print("".join(encrypted_text))