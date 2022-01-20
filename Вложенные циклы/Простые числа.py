n = int(input())
a = []
for i in range(2, n):
    d = False
    for j in range(2, i):
        if i % j == 0:
            d = True
    if not d:
        a.append(i)
for k in a:
    print(k)