s = input().split()
s1 = input().split()
s2 = input().split()
summ = 0
a = []
for i in range(len(s2)):
    if s2[i] in s1 and s2[i] not in s and s2[i] not in a:
        summ += int(s2[i])
        a.append(s2[i])
print('; '.join(a))
print(summ)
