banned_words = input().split(", ")
text = input()

for word in banned_words:
    if word in text:
        block = '*' * len(word)
        text = text.replace(word, block)

print(text)




