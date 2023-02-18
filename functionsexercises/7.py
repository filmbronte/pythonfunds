x = input().split()
lst = []
for num in x:
    lst.append(int(num))

print(f"The minimum number is {min(lst)}")
print(f"The maximum number is {max(lst)}")
print(f"The sum number is: {sum(lst)}")
