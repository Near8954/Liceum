n = int(input())
for i in range(1, n + 1):
    for j in range(i - 1, 0, -1):
        print('Осталось секунд:', j)
    print('Осталось секунд:', 0)
    print('Пуск', i)