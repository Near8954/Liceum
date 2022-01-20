n  = int(input())
for i in range(n):
    s = input()
    if 'кот' in s:
        print(i + 1, s.find('кот') + 1)