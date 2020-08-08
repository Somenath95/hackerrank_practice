import re
# print(sum(map(str.isupper, input())) + 1)
s = input()
print(len(re.findall(r'[A-Z]', s)) + 1)