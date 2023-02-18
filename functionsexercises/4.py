def Sum(n):
    even_sum = 0
    odd_sum = 0
    for i in n:
        num = int(i)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


n = input()
print(Sum(n))

