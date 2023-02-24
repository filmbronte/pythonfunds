from collections import deque
#
# example_q = deque()
#
# example_q.append(1)
# example_q.append(2)
# example_q.append(3)
# example_q.append(4)
#
# # example_q = deque([1, 2, 3, 4])
#
# while example_q:
#     print(example_q.popleft())

example_queue = deque()
example_stack = []

for i in range(1, 6):
    example_queue.append(i)
    example_stack.append(i)

print("Queue")
while example_queue:
    print(example_queue.popleft())

print("Stack")
while example_stack:
    print(example_stack.pop())

# q = []
#
# for i in range(1, 6):
#     q.append(i)
#
# while q:
#     print(q.pop(0))
