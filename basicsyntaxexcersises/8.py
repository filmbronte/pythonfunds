coffee = 0

while True:
    command = input()
    if command == "END":
        break

    if command == "coding" or command == "movie" or command == "cat" or command == "dog":
        coffee += 1
    elif command == "CODING" or command == "MOVIE" or command == "CAT" or command == "DOG":
        coffee += 2

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)

