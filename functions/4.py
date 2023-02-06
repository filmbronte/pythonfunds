"""Write a function that receives a string and a counter n.
The function should return a new string – the result of repeating the old string n times.
Print the result of the function.
Try using lambda"""

old_string = input()
counter = int(input())

# def repetition(string, n):
#     # for _ in range(1, counter + 1):
#     #     print(old_string, end="")

repeat_string = lambda a, b: a * b

result = repeat_string(old_string, counter)
print(result)
