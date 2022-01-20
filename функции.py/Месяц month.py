def month_name(n, lg):
    month_rus = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 
                 6: 'июнь', 7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
    month_eng = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 
                 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    if lg == 'en':
        return month_eng[n]
    else:
        return month_rus[n]
print(month_name(3, 'ru'))