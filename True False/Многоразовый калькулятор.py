n = ''
f = 1
while n != 'x':
    n = input()
    do = input()
    if do == 'x':
        print(n)
        break
    if do == '!':
        if int(n) >= 0:
            for i in range(1, int(n) + 1):
                f *= i
            print(f)
            f = 1
    elif do == '+':
        n2 = int(input())
        print(int(n) + n2)
    elif do == '-':
        n2 = int(input())
        print(int(n) - n2)
    elif do == '*':
        n2 = int(input())
        print(int(n) * n2)
    elif do == '%':
        n2 = int(input())
        if n2 != 0:
            print(int(n) % n2)
    elif do == '/':
        n2 = int(input())
        if n2 != 0:
            print(int(n) // n2)

