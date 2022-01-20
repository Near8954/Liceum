s = input()
c = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
    else:
        print(c, s[i])
        c = 1
print(c, s[-1])