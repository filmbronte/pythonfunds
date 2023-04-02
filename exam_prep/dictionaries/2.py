text = input().split()
products = {}
searched_products = input().split()

for i in range(0, len(text), 2):
    products[text[i]] = int(text[i + 1])
    # print(products)

for product in searched_products:
    if product in products.keys():
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

