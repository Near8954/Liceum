n = int(input())
s = []
for i in range(n):
    s.append(input())
for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(s[j]) > len(s[j + 1]):
            s[j], s[j + 1] = s[j + 1], s[j]
        elif len(s[j]) == len(s[j + 1]):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
for i in range(n):
    print(s[i])
