def tic_tac_toe(field):
    for i in field:
        if i.count('x') == 3:
            print('x win')
            return
        elif i.count('0') == 3:
            print('0 win')
            return
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] == 'x' or\
                field[0][0] == field[1][1] == field[2][2] == 'x' or\
                field[0][2] == field[1][1] == field[2][0] == 'x':
            print('x win')
            return
        elif field[0][i] == field[1][i] == field[2][i] == '0' or\
                field[0][0] == field[1][1] == field[2][2] == '0' or\
                field[0][2] == field[1][1] == field[2][0] == '0':
            print('0 win')
            return
    print('draw')
data="""x 0 -
x - 0
x 0 -"""

field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)
        

        