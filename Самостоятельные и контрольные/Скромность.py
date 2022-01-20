s = input().split(', ')
lenth = int(input())
for i in range(len(s)):
    if len(s[i]) <= lenth:
        print(s[i].lower(), end=' ')