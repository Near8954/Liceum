mon = int(input())
n = int(input())
for i in range(1, n + 1):
    for j in range(n - i + 1):
        for k in range(n - j):
            if i * 20 + j * 10 + k * 5 == mon and i + k + j == n:
                print(i, j, k)

