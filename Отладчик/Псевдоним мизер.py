k = int(input())
while k != 0:
    if k <= 4:
        k2 = max(k - 1, 1)
    else:
        k2 = max(k % 4 - 1, 1)
    k -= k2
    print(k2, k)
    if k == 0:
        print('Вы выиграли!')
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
        print('ИИ выиграл!')
