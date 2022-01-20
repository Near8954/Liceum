s = input()
s = s.lower()
a = []
an = []
maxlet = ''
maxnum = 0
for i in s:
    if i not in a and i != ' ':
        a.append(i)
for i in a:
    an.append(s.count(i))
for i in range(len(an)):
    if an[i] > maxnum:
        maxnum = an[i]
        maxlet = a[i]
    elif an[i] == maxnum:
        if a[i] < maxlet:
            maxlet = a[i]
            maxnum = an[i]
print(maxlet)