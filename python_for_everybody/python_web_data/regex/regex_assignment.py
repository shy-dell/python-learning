import re

lst = []

file = open('regex_assignment.txt')
for line in file:
    x = re.findall(r'(\d+)',line)
    if not x:
        continue
    else:
        for num in x:
            y = int(num)
            lst.append(y)

total = sum(lst)
print(total)