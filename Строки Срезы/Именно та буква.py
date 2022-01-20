s = input()
n = int(input())
s2 = input()
if n < 1 or n > len(s):
    print('ОШИБКА')
elif len(s2) > 1:
    print('ОШИБКА')
else:
    if s[n - 1] == s2:
        print('ДА')
    else:
        print('НЕТ')