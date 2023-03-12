# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)

text = input()

for i in range(len(text)):
    if text[i] == ":":
        print(f"{text[i]}{text[i+1]}")


