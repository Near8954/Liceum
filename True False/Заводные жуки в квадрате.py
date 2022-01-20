lenth = float(input())
speed = float(input())
c = 0
while round(lenth - speed, 2) > 0.01:
    lenth = round((speed ** 2 + (lenth - speed) ** 2) ** 0.5, 2)
    c += 1
    print(lenth)
print(c)