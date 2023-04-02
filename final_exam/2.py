import re

n = int(input())
pattern = r"^(\$|\%)([A-Z][a-z]{2,})\1: (\[[0-9]+\])\|(\[[0-9]+\])\|(\[[0-9]+\])\|$"

for _ in range(n):
    data = input()
    result = re.findall(pattern, data)

    if result:
        for match in result:
            n1 = ''.join(re.findall(r"\[([0-9]+)]", match[2]))
            n2 = ''.join(re.findall(r"\[([0-9]+)]", match[3]))
            n3 = ''.join(re.findall(r"\[([0-9]+)]", match[4]))
            final_result = chr(int(n1)) + chr(int(n2)) + chr(int(n3))
            print(f'{match[1]}: {final_result}')
    else:
        print("Valid message not found!")
