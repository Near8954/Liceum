s = input(). split(' - ')
t = list('computer')
c = 0
a = []
while 'HELLO' not in t:

    for i in range(len(s)):
        if 'HELLO' in s:
            break
        for elem in s[i]:
            if elem.lower() in t:
                c += 1
        if c <= 3:
            a.append(s[i])
        c = 0
        a.sort(reverse = False)
        for j in range(len(a)):
            print(str(a[j]).upper() if c % 3 == 0 else a[j], end=' ')
            c += 1
        c = 0
        a = []
    s = input(). split(' - ')
