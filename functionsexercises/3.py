# n1 = int(input())
# n2 = int(input())
#
# for ch in range(n1, n2 + 1):
#     print(chr(ch), end=" ")

def ascii_characters(a, b):
    result = []
    for ch in range(ord(a) + 1, ord(b)):
        result.append(chr(ch))

    return result


a = input()
b = input()

# n1 = int(input())
# n2 = int(input())
#
# for ch in range(ord(a) + 1, ord(b)):
#     print(chr(ch))

print(" ".join(ascii_characters(a, b)))

