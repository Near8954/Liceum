s = input()
line1 = ''
line2 = ''
line3 = ''
line4 = ''
line5 = ''
A = [' *   ','* *  ', '***  ', '* *  ', '* *  ']
B = ['**   ','* *  ','**   ','* *  ','**   ']
C = [' *   ','* *  ','*    ','* *  ',' *   ']
for i in s:
    if 'A' ==  i:
        line1 += A[0]
        line2 += A[1]
        line3 += A[2]
        line4 += A[3]
        line5 += A[4]
    elif 'B' == i:
        line1 += B[0]
        line2 += B[1]
        line3 += B[2]
        line4 += B[3]
        line5 += B[4]
    elif 'C' == i:
        line1 += C[0]
        line2 += C[1]
        line3 += C[2]
        line4 += C[3]
        line5 += C[4]
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)