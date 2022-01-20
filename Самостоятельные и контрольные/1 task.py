s = input()
summ = 0
while s != '---':
    if 'dragon' in s:
        summ += len(s)
    s = input()
print(summ)