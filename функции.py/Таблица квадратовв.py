def squared(a, b, k):
    if (b - a) / 10 > int((b - a) / 10):
        x = (b - a) // 10 + 1
    else:
        x = (b - a) // 10
    while a < b:
        for i in range(x):
            for j in range(10):
                if a ** 2 % k != 0:
                    print(f"{a ** 2:<4}", end = ' ')
                    a += 1
                else:
                    a += 1
                    continue
            print()
squared(11, 99, 10)