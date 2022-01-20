s = input()
summ = 0
while 'Гэндальф' not in s:
    if 'волшебн' in s:
        summ += len(s)
    s = input()
print(summ)