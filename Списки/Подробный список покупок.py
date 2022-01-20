a = []
for i in range(int(input())):
    a.append(input() + ' ' + input())
for i in range(len(a) - 1, 0, -1):
    print(a[i])
print(a[0])

