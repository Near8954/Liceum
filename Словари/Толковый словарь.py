n = int(input())
slov = dict()
for i in range(n):
    s = input().split()
    slov[s[0]] = s[1:]
n = int(input())
for i in range(n):
    s = input()
    if s in slov:
        print(*slov[s])
    else:
        print('Нет в словаре')
