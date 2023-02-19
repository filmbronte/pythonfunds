shelf = input().split("&")

while True:
    line = input()
    if line == "Done":
        break

    command_args = line.split(" | ")
    command = command_args[0]
    book_name = command_args[1]

    if command == "Add Book":
        if book_name not in shelf:
            shelf.insert(0, book_name)
    elif command == "Take Book":
        if book_name in shelf:
            shelf.remove(book_name)
    elif command == "Swap Books":
        book = book_name
        new_book = command_args[2]
        if book in shelf and new_book in shelf:
            idx1 = shelf.index(book)
            idx2 = shelf.index(new_book)
            shelf[idx1], shelf[idx2] = shelf[idx2], shelf[idx1]

    elif command == "Insert Book":
        if book_name not in shelf:
            shelf.append(book_name)
    elif command == "Check Book":
        idx = int(book_name)
        if len(shelf) >= idx:
            print(shelf[idx])

print(", ".join(shelf))
