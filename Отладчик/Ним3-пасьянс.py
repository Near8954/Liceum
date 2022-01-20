k1 = int(input())
k2 = int(input())
k3 = int(input())
while not(k1 == 0 and k2 == 0 and k3 == 0):
    nk = int(input())
    kk = int(input())
    if nk == 1:
        print(k1 - kk, k2, k3)
        k1 -= kk
    elif nk == 2:
        print(k1, k2 - kk, k3)
        k2 -= kk
    elif nk == 3:
        print(k1, k2, k3 - kk)
        k3 -= kk