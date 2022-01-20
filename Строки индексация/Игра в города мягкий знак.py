str = input()
str2 = input()
if str[-1] == str2[0] or (str[-1] == 'ь' and str[-2] == str2[0]):
    print('ВЕРНО')
else:
    print('НЕВЕРНО')