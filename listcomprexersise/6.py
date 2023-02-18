number = int(input())
result = []
while number > 0:
    n = len(result) + 1
    shell_value = min(2 * (n**2), number)
    result.append(shell_value)
    number -= shell_value

print(result)

