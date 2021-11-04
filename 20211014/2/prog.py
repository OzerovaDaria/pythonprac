from math import *
import numpy as np

def scale(A, B, a, b, x):
    return (x - A)/(B - A)*(b-a) + a
def ff(x):
    return -eval(F)
def print_mas(mas):
    for i in mas:
        print("".join(i))

    
x0, x1, y0, y1 = eval(input())
F = input()
mas = []
W, H = 80, 20 #int(input()), int(input())
for i in range(W + 1):
    mas.append([" " for j in range(H + 1)])

i = x0
while True:
    if i >= x1: break
    a = round(scale(x0, x1, 0, W, i))
    b = round(scale(y0, y1, 0, H, ff(i)))
    mas[a][b] = "*"
    i += (x1 - x0) / W
mas = np.transpose(mas)
print_mas(mas)
    
"""
A, B = -4, 4
X = [scale(0, W+1, -4, 4, i) for i in range(W+1)]
Y = [F(x) for x in X]
my, My = min(Y), max(Y)
for y in Y:
    print( int(scale(my, My, 0, W+1, y))*" "+"*" )
"""







