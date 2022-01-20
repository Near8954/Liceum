def convert(s):
    k = ord(s[0]) % 65 + 1, int(s[1])
    return k


def reconvert(bukva, cifra):
    bukva = chr(bukva + 64)
    return bukva + str(cifra)


def possible_turns(s):
    itog = []
    z = [[2, -1], [-2, -1], [1, -2], [-1, -2], 
         [2, 1], [1, 2], [-2, 1], [-1, 2]]
    x, y = convert(s)
    for i in z:
        if x - i[0] <= 8 and x - i[0] >= 1 \
            and y - i[1] <= 8 and y - i[1] >= 1:
            itog.append(reconvert(x - i[0], y - i[1]))
    return sorted(itog)
print(possible_turns('H8'))
