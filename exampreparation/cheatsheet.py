# # def find_idx(seq, element):
# #     for idx in range(len(seq)):
# #         if seq[idx] == element:
# #             return True
# #
# #     return False
#
# #
# # nums = [1, 2, 3, 4, 5, 6]
# # new = list(reversed(nums))
# # print(nums[::-1])  # both reverse the list
# # print(new)
# #
# # # reversing a string
# # print("Hello"[::-1])
# #
# # # list(map(int, string_list)) is the same as [int(el) for el in string_list]
# # # list(map(lambda x: x*2, numbers_list)) is the same as [el * 2 for el in numbers_list]
# #
# # # list(filter(lambda x: x % 2 == 0, numbers_list)) is the same as
# # # [el for el in numbers_list if el % 2 == 0]
# #
# # numbers = list(map(int, input().split(", ")))
# # print(list(filter(lambda x: x % 2 == 0, numbers)))
# # # prints all even numbers
#
# def find_idx(seq, element, target_idx):
#     count = 0
#     for idx in range(len(seq)):
#         if seq[idx] == element:
#             count += 1
#             if count == target_idx:
#                 return idx
#
#     return -1
#
#
# print(find_idx([1, 2, 3, 3, 3, 4, 5], 3, 3))
#
#

import math

print(math.floor(2.403))
