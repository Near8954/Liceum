s = []
for i in range(3):
    s.append(input())
for i in range(3 - 1):
    for j in range(3 - 1 - i):
        if len(s[j]) > len(s[j + 1]):
            s[j], s[j + 1] = s[j + 1], s[j]
c = len(s[0])
b = len(s[1])
a = len(s[2])
for i in range(a, b-1, -c):
    print(i, end=' ')
