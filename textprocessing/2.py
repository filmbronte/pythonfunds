txt = input().split()
result = ''

for i in txt:
    n = len(i)
    final = i * len(i)
    result += final

print(result)
