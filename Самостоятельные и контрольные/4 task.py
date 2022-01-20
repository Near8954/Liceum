n = int(input())
a = []
summ = 0
maxi = []
mmm = []
f = False
for i in range(n):
    a.append(list(map(int, input().split(','))))
for i in a:
    if not f:
        do = int(input())
        if do == 0:
            for s in i:
                if abs(s) > 1000:
                    f = True
                    print('TOO BRIGHT')
                    break
                summ += s
                mmm.append(summ / len(i))
            summ = 0
            c = 0
        elif do == 1:
            for s in i:
                if abs(s) > 1000:
                    f = True
                    print('TOO BRIGHT')
                maxi.append(s)
                mmm.append(max(maxi))
            maxi = []
        elif do == -1:
            for s in i:
                if abs(s) > 1000:
                    f = True
                    print('TOO BRIGHT')
                    break
                maxi.append(s)
                mmm.append(min(maxi))
            maxi = []
mmm.sort()
print(*mmm, sep='\n')
