n = int(input())
a = []
b = []
f = []
for i in range(n):
    a.append(input())
n = int(input())
for j in range(n):
    b.append(input())
for j in b:
    if j in a:
        f.append(j)
for j in f:
    print(j)
