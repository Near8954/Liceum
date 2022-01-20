from pickle import LONG


def catalan(n: LONG) -> LONG:
    if n == 0:
        return 1
    c = (2 * (2 * n - 1) / (n + 1) * catalan(n - 1))
    return c
print(catalan(45))