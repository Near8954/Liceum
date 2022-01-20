s = input().split()
slov = dict()
for i in range(len(s)):
    if s[i] not in slov:
        slov[s[i]] = 1
    else:
        slov[s[i]] += 1
    print(slov[s[i]], end=' ')
