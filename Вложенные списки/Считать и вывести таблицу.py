n = int(input())
m = int(input())
table = [[input() for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(table[i][j], end='\t')
    print()
