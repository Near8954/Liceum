n = int(input())
for i in range(1, n + 1):
    for j in range(i, n + 1):
        x = j ** 2 - i ** 2
        y = 2 * i * j
        z = j ** 2 + i ** 2
        if x % 2 == 0 and y % 2 == 0 \
            or y % 2 == 0 and z % 2 == 0 or z % 2 == 0 and x % 2 == 0:
            continue
        if x % 3 == 0 and y % 3 == 0 \
            or y % 3 == 0 and z % 3 == 0 or z % 3 == 0 and x % 3 == 0:
            continue
        if n >= x > 0 and n >= y > 0 and n >= z > 0:
            print(x, y, z)

        
