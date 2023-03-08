def mining():
    d = {}

    while True:
        resource = input()

        if resource == "stop":
            break

        quantity = int(input())

        if resource not in d:
            d[resource] = quantity
        else:
            d[resource] += quantity

    for key, value in d.items():
        print(f"{key} -> {value}")


mining()
