from collections import defaultdict

words = input().split()
word_counter = defaultdict(int)

for word in words:
    word_counter[word.lower()] += 1

print(" ".join([word for word, count in word_counter.items() if count % 2 == 0]))