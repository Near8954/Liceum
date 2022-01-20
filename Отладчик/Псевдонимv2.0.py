k = int(input())
while k != 0:
    if k % 4 == 0:
        k-=1
        print(1, k)
    else:
        print(k - k // 4 * 4, end=' ')
        k = k // 4 * 4
        print(k)
    if k == 0:
        print('ИИ выиграл!')
        break
    while True:
        k1 = int(input())
        if k1 > 3 or k1 < 1 or k1 > k:
            print('Некорректный ход:', k1)
        else:
            print(k1, k - k1)
            k = k - k1
            break
    if k == 0:
        print('Вы выиграли!')
