small = 1
big = 1001
print(500)
s = input()
while s != '=':
    if s == '>':
        small = round(small + (big - small) // 2)
    elif s == '<':
        big = round(big - (big - small) // 2)
    if s == '<':
        print(int(small + (big - small) // 2))
    else:
        print(round(small + (big - small) // 2))
    s = input()