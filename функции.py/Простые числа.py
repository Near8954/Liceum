def prime(n):
    f = True
    for i in range(2, n):
        if n % i == 0:
            f = False
            break
    if f:
        return 'Простое число'
    else:
        return 'Составное число'
print(prime(4))

        