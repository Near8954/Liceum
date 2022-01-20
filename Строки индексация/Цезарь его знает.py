step = int(input())
s = input()
s_end = ''
for i in s:
    if ord(i) >= ord('а') and ord(i) <= ord('я'):
        if ord(i) + step > ord('я'):
            s_end += chr(ord(i) + step - 32)
        else:
            s_end += chr(ord(i) + step)
    elif ord(i) >= ord('А') and ord(i) <= ord('Я'):
        if ord(i) + step > ord('Я'):
            s_end += chr(ord(i) + step - 32)
        else:
            s_end += chr(ord(i) + step)
    else:
        s_end += i
print(s_end)