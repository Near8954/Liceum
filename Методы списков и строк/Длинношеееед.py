s = input().lower()
maxn = 0
for i in s:
    if s.count(i) > maxn:
        maxn = s.count(i)
print(maxn)
