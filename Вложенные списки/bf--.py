s = input()
n = [0 for i in range(30000)]
k = 1
for i in range(len(s)):
    if s[i] == '>':
        k = (k + 1) % 30000
    elif s[i] == '<':
        k -= 1
        if k < 0:
            k += 30000
    elif s[i] == '+':
        n[k] += 1
        if n[k] == 256:
            n[k] = 0
    elif s[i] == '-':
        n[k] -= 1
        if n[k] < 0:
            n[k] = 255
    elif s[i] == '.':
        print(n[k])
