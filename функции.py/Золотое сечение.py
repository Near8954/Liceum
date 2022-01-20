def golden_ratio(i):
    n1 = 0
    n2 = 1
    for j in range(i):
        n1, n2 = n2, n1 + n2
    print(n2 / n1)
