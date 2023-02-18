def isFound(a, b):
    for i in b:
        found = a in i
        if found:
            return True

    return False


one = input().split(", ")
two = input().split(", ")
three = [x for x in one if isFound(x, two)]
print(three)
