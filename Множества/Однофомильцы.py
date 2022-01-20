n = int(input())
set_ = set()
set_1 = set()
k = 0
for i in range(n):
    s = input()
    if s in set_ and s not in set_1:
        k += 2
        set_1.add(s)
    elif s in set_ and s in set_1:
        k += 1
    else:
        set_.add(s)
print(k)