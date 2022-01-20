s = input()
n = s[:4]
mist = []
summall = 0
for i in n:
    n = n.replace(' ','')
n = int(n)
sump = int(s[4:])
for i in range(n):
    s = input()
    st = int(s[:7].replace(' ', ''))
    k = int(s[8:s.find('=')].replace(' ', ''))
    summ = int(s[s.find('=') + 1:])
    if k * st != summ:
        mist.append(i + 1)
    summall += k * st
if summall != sump:
    print(sump - summall)
    for i in mist:
        print(i, end=' ')
else:
    print(0)
