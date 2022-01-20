n = int(input())
names = []
for i in range(n):
    names.append(input())
step = int(input())
k = int(input())
for i in range(k):
    del names[step - 1::step]
for i in names:
    print(i)
