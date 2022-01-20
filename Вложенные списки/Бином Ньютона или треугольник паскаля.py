n = int(input())
start = [1, 1]
if n == 1:
    print(1)
elif n == 2:
    print(1)
    print(*start)
else:
    print(1)
    print(*start)
    for i in range(1, n - 1):
        newstart = []
        newstart.append(1)
        for j in range( len(start) - 1):
            newstart.append(start[j] + start[j + 1])
        newstart.append(1)
        start = newstart
        print(*start)