s = input().split(':')
a = []
c = 1
while s != '':
    if c == 0:
        s = s.split(':')
    a.append([s[0], s[1], str(s[4].split(',')[0])])
    s = input()
    c = 0
s = input().split(';')
for i in range(len(a)):
    if a[i][1] in s:
        print('To:', a[i][0])
        print(f'{a[i][2]}, ваш пароль слишком простой, смените его.')