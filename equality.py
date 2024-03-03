import re

file = open('equality.txt', 'r')
lines = file.readlines()
groups = ""

for line in lines:
    pattern = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', line)
    if len(pattern) > 0:
        for i in pattern:
            groups += i[4]
        
print(groups)