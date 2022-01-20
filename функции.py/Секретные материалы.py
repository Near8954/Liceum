def print_document(pages):
    a = []
    f = False
    for i in pages:
        if i.startswith('Секретно'):
            f = True
            break
        else:
            a.append(i)
    print('\n'.join(a))
    if f:
        print('Дальнейшие материалы засекречены')
    else:
        print('Напечатано без купюр')
print_document(["Пустой трёп", "который", "никому не интересен"])
    

