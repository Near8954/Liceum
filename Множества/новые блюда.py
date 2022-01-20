m = int(input())
menu = set()
isp = set()
for i in range(m):
    s = input()
    menu.add(s)
n = int(input())
for i in range(n):
    kd = int(input())
    for j in range(kd):
        s = input()
        isp.add(s)
menu = menu - menu.intersection(isp)
for i in menu:
    print(i)
