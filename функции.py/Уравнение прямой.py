def equation(a, b):
    x1, y1 = map(float, a.split(';'))
    x2, y2 = map(float, b.split(';'))
    if x1 == x2:
        print(x1)
        return
    elif y1 == y2:
        print(y1)
        return
    else:
        k = (y1 - y2) / (x1 - x2)
        if x1 == 0 or x2 == 0:
            b = 0.0
        else:
            b = y2 - k * x2
        print(k, b)
