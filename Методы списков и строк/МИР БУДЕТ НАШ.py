s = input().upper()
s_end = ''
for i in range(len(s) - 1):
    if s[i + 1] != ' ' and s[i] != ' ':
        s_end += s[i] + '-'
    else:
        s_end += s[i]
print(s_end + s[-1])