n = int(input())
a = []
for i in range(n):
    s = int(input())
    a.append(s)
mini = int(input())
maxi = int(input())
for j in range(len(a)):
    if a[j] >= mini and a[j] <= maxi:
        print(a[j])