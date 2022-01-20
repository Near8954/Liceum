n = int(input())
things = [input() for i in range(n)]
k = int(input())
for i in range(k):
    x = int(input())
    t = []
    for j in range(1, x + 1):
        y = int(input())
        t.append(things[y - 1])
    things = t
print(*things, sep='\n')
