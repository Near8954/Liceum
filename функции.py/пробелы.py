def space_game(text):
    k = text.count(' ')
    if k % 2 == 0:
        print('Вы выиграли')
    else:
        print('Вы проиграли')