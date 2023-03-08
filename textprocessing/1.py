while True:
    txt = input()

    if txt == "end":
        break

    reversed_txt = txt[::-1]
    print(f"{txt} = {reversed_txt}")
