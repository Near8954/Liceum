s = input().split()
summ = 0
n, m = map(int, input().split())
for i in range(n, m + 1):
    summ += int(s[i]) ** 2
print(summ)
