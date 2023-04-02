text = input().split()

# products = {}
#
# for i in range(0, len(text), 2):
#     products[text[i]] = int(text[i+1])

products = {text[i]: int(text[i+1]) for i in range(0, len(text), 2)}

print(products)
