dictionary1 = {
    'test1': 'value',
    'numbers1': 'one',
    'letters1': 'a',
    'symbols1': '@'
}

dictionary2 = dict([
    ('test2', 'value'),
    ('numbers2', 'one'),
    ('letters2', 'a'),
    ('symbols2', '@')
])

letters = ['a', 'b', 'c', 'd']
nums = [1, 2, 3, 4]
dictionary3 = dict(zip(letters, nums))

print(dictionary1)
print(dictionary2)
print(dictionary3)
dictionary4 = {**dictionary1, **dictionary2, **dictionary3}
print(dictionary4)
