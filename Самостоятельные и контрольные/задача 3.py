n = int(input())
key = input()
c = 0
for i in range(n):
    s = input()
    if 'забыл' in s or key in s:
        c += 1
if c > n * 0.5:
    print('ВСЕ РАВНО НИЧЕГО СТРАШНОГО', c + n, sep='\n')
else:
    print('НЕ ТАК И МНОГО', n + c, sep='\n')
