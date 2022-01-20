k1 = int(input())
k2 = int(input())
while not(k1 == 0 and k2 == 0):
    nk = int(input())
    kk = int(input())
    if nk == 1:
        print(k1 - kk, k2)
        k1 -= kk
    else:
        print(k1, k2 - kk)
        k2 -= kk

