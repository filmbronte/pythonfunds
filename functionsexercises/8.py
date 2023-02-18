x = input().split(", ")


def is_palindrome(x):
    return x == x[::-1]


for i in x:
    print(is_palindrome(i))

