def roots_of_quadratic_equation(a, b, c):
    if a == b == c == 0:
        return ['all']
    elif a == b == 0:
        return []
    elif a == 0:
        return [-c / b]
    else:
        D = b ** 2 - 4 * a * c
        if D > 0:
            x1, x2 = (-b - D ** 0.5) / (2 * a), (-b + D ** 0.5) / (2 * a)
            return [x1, x2]
        elif D == 0:
            return [-b / (2 * a)]
        else:
            return []
result = roots_of_quadratic_equation(2, -8, 8)
print(*sorted(result))
    