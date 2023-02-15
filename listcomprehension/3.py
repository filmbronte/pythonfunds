notes = [0] * 10  # creating an empty list with zeros, so we can fill it up later
command = input()

while command != "End":
    importance, task = command.split("-")  # splits them with "-"
    importance = int(importance)  # has to be a number, so we turn it into an integer
    index = importance - 1  # importance is 6 for example, so we have to put it in the 5th index
    notes[index] = task  # task is then placed in the [index] part of the list
    command = input()

# removes the zeros in the list
print([task for task in notes if task != 0])


