first_line = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for i in range(len(first_line)):
    beggar_index = i % beggars_count
    num = int(first_line[i])
    beggars[beggar_index] += num

print(beggars)