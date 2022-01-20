x = 0
y = 0
look = 1
xk = int(input())
yk = int(input())
flag = True
c = 0
while flag:
    c += 1
    n = input()
    if n == 'налево':
        look -= 1
        if look == 0:
            look = 4
    if n == 'направо':
        look += 1
        if look > 4:
            look = 1
    if n == 'разворот':
        if look == 1:
            look = 3
        elif look == 2:
            look == 4
        elif look == 4:
            look = 2
        elif look == 3:
            look = 1
    if n == 'вперёд':
        k = int(input())
        if look == 1:
            y += k
        elif look == 2:
            x += k
        elif look == 3:
            y -= k
        elif look == 4:
            x -= k
        if xk == x and yk == y:
            flag = False
            endc = c
            endn = look
print(endc)
if look == 1:
    print('север')
elif look == 2:
    print('восток')
elif look == 3:
    print('юг')
elif look == 4:
    print('запад')
    


    

