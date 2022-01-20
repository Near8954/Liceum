def bracket_check(test_string):
    opened = 0
    f = True
    for c in test_string:
        if c == '(':
            opened += 1
        elif c == ')':
            opened -= 1
        if opened < 0:
            f = False
            break
    if f and opened == 0:
        print('YES')
    else:
        print('NO')

