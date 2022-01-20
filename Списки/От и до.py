n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
ot = int(input())
do = int(input())
if ot == 0 and do == len(a):
    print(sum(a))
elif ot == 0:
    print(sum(a[:do]))
elif do == 0:
    print(sum(a[ot:]))
else:
    print(sum(a[ot - 1:do]))