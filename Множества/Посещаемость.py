M = int(input())
set_ = set()
set_1 = set()
for i in range(M):
    N = int(input())
    if i == 0:
        for j in range(N):
            set_.add(input())
    else:
        for j in range(N):
            set_1.add(input())
        set_ = set_.intersection(set_1)
        set_1.clear()
print()
for i in set_:
    print(i)

