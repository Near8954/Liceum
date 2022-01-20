n = int(input())
m = int(input())
table = [[input() for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(table[i][j], end='\t')
    print()
print()
for i in range(m):
    for j in range(n):
        print(table[j][i], end='\t')
    print()