n = int(input())
np = n
n2 = int(input())
while n2 != 0:
    if np - n2 > 0:
        np, n2 = n2, int(input())
        