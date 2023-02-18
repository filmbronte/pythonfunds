def aliquotSum(n):
    proper_divisors = []

    for i in range(1, n):
        if n % i == 0:
            proper_divisors.append(i)

    if sum(proper_divisors) == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(aliquotSum(number))
