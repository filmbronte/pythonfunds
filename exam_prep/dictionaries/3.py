products = {}

while True:
    text = input()
    if text == "statistics":
        break

    command = text.split(": ")

    product = command[0]
    quantity = int(command[1])

    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
