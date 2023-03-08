secret_message = [word for word in input().split()]

for el in secret_message:
    result = ''
    result_word = []
    for x in el:
        if x.isnumeric():
            result += str(x)
        elif x.isalpha():
            result_word.append(x)
    result_word[0], result_word[-1] = result_word[-1], result_word[0]
    secret = chr(int(result))
    print(secret + "".join(result_word), end=" ")


