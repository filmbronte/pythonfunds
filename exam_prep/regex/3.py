# /\d{2}\/[A-Z][a-z]+\/\d{4}|\d{2}\.[A-Z][a-z]+\.\d{4}|\d{2}\-[A-Z][a-z]+\-\d{4}
# /\d{2}\/[A-Z]{1}[a-z]{2}+\/\d{4}|\d{2}\.[A-Z]{1}[a-z]{2}+\.\d{4}|\d{2}\-[A-Z]{1}[a-z]{2}+\-\d{4}
#
import re

dates = input()
pattern = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'
result = re.findall(pattern, dates)

for match in result:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')

