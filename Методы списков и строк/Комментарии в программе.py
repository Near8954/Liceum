s = input()
n = int(s[1:])
for i in range(n):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    while s.endswith(' '):
        s = s[:-1]
    print(s)