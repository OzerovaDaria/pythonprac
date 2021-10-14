from math import *

def scale(A, B, a, b, x):
    return (x - A)/(B - A)*(b-a) + a

F = sin
W, H = 66, 20 #int(input()), int(input())
A, B = -4, 4
X = [scale(0, W+1, -4, 4, i) for i in range(W+1)]
Y = [F(x) for x in X]
my, My = min(Y), max(Y)
for y in Y:
    print( int(scale(my, My, 0, W+1, y))*" "+"*" )
