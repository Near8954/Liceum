spr = set()
for i in range(int(input())):
    spr.add(input())
for i in range(int(input())):
    dish = input()
    spspr = set()
    for j in range(int(input())):
        spspr.add(input())
    if len(spspr.intersection(spr)) == len(spspr):
        print(dish)

