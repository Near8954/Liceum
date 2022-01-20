s = input()
c = 0
for i in s:
    if i != ' ' and i != '\t':
        c += 1
print(c)