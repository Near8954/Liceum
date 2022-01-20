def ask_password():
    f = False
    for i in range(3):
        passw = input()
        if passw == 'password':
            f = True
    if f:
        print('Пароль принят')
    else:
        print('В доступе отказано')
