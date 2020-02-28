import re
n = int(input())
s = input()

unique = set(s)
for i in unique:
    s = re.sub(i+'+',i,s)
print(len(s))