def line(s, t):
    x, y = map(float, t.split(';'))
    x1k = float(s[:s.find('x')]) * x
    if s[s.find('x') + 1] == '+':
        y1 = x1k + float(s[s.rfind('+') + 1:])
    else:
        y1 = x1k - float(s[s.rfind('-') + 1:])
    print(y1 == y)
line("-0.24x-9.4", "8.6;-11.464")