# # import re
# #
# # line = input()
# # regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# # x = re.findall(regex, line)
# # print(" ".join(x))
#
#
# import re
#
# line = input()
# pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
# x = re.findall(pattern, line)
# print(", ".join(x))

import re

text = "I love Shiki and shiki is my cat."
pattern = re.findall(r"Shiki", text, re.IGNORECASE)
print(pattern)
