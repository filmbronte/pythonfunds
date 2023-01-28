input_string = input().split()
# split() puts input string into a list
lst = []

for i in input_string:
    number = int(i)
    lst.append(-number)

print(lst)
