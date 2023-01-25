tail = input()
body = input()
head = input()

x = [tail, body, head]
x[0], x[2] = x[2], x[0]
print(x)

