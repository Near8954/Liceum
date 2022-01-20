def take_large_banknotes(banknotes):
    s = [str(i) for i in banknotes if i > 10]
    return str(' '.join(s))
print(take_large_banknotes([500, 100, 100, 1000, 50]))