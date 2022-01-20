n = int(input())
table = [input().split(',') for i in range(n)]
n = int(input())
for i in range(n):
    x = list(map(int, input().split(',')))
    print(table[x[0]][x[1]])