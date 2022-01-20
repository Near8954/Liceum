def number_in_english(number):
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 
        4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    dec = {2: 'twenty ', 3: 'thirty ', 4: 'fourty ', 
        5: 'fifty ', 6: 'sixty ', 7: 'seventy ', 8: 'eighty ', 9: 'ninety '}
    iscl = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    if len(str(number)) == 1:
        return d[number]
    elif len(str(number)) == 2:
        if number in iscl:
            return iscl[number]
        elif number % 10 == 0:
            return dec[number // 10]
        else:
            return dec[number // 10] + d[number % 10]
    else:
        if number % 100 == 0:
            return d[number // 100] + ' hundred'
        elif number % 100 in iscl:
            return d[number // 100] + ' hundred and ' + iscl[number % 100]
        elif number % 10 == 0 and number // 10 % 10 != 0:
            return d[number // 100] + ' hundred and ' + dec[number // 10 % 10]
        elif number % 10 != 0 and number // 10 % 10 == 0:
            return d[number // 100] + ' hundred and ' + d[number % 10]
        else:
            return d[number // 100] + ' hundred and ' + \
                dec[number // 10 % 10] + d[number % 10]
for i in range(1000):
    print(number_in_english(i).lower())
