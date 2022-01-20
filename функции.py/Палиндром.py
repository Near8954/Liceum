def palindrome(s):
    s = s.lower().replace(' ', '')
    if s == s[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'
print(palindrome('А роза упала на лапу Азора'))