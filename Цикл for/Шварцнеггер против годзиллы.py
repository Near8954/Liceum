n = int(input())
ch = int(input())
zn = int(input())
znk = 0
chk = 0
znk += zn
for i in range(n - 1):
    ch = int(input())
    zn = int(input())
    while zn != znk:
        if zn > znk:
            zn -= znk
        else:
            znk -= zn
    