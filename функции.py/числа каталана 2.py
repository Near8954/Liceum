def catalan_(n, d):
    result = 0
    if d.get(n):
        return d[n]
    else:
        for i in range(n):
            result += catalan_(i, d) * catalan_(n - 1 - i, d)
        d[n] = result
        return result


def catalan(n):
    d = {0: 1}
    return catalan_(n, d)


print(catalan(45))
