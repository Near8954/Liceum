s = input()
s_end = ''
for i in s:
    s_end = s_end + str(ord(i)) + ', '
print(s_end[:len(s_end) - 2])
