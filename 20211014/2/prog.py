from math import *
def mass(aa, bb, a, b, x):
    return (x - aa)/(bb - aa) * (b - a) + a
def make (ww, H, strn, y_num):
    for i in range(ww):
        for j in range(H):
            if H - j - 1 == y_num[i]:
                strn[j] += '*'
            else:
                strn[j] += ' '
    return strn
ww, H, a, b, s = input().split()
ww, H, a, b = int(ww), int(H), int(a), int(b)
f = lambda x: eval(s)
X = [mass(0, ww, a, b, i) for i in range(ww)]
Y = [f(x) for x in X]
my, My = min(Y), max(Y)
y_num = [int(mass(my, My, 0, H, f(x))) for x in X]
strn = ['' for _ in range(H)]
strn = make(ww, H, strn, y_num )
for st in strn:
    print(st)
