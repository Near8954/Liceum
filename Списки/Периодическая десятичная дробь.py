n = int(input())
period = []
ostatki = []
ost = 1
while ost not in ostatki:
    ostatki.append(ost)
    period.append(ost // n)
    ost = ost % n * 10
k = 0
for i in ostatki:
    if i == ost:
        break
    k += 1
print(*period[k:], sep='')