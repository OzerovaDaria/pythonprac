def Calc(s, t, u):
    def f(x, y):
        return eval(u)
    def f1(x):
        return eval(s)
    def f2(x):
        return eval(t)
    def res(x):
        return f(f1(x), f2(x))
    return res
a, b, c = eval(input())
x = eval(input())
from math import *
F = Calc(a, b, c)
print(F(x))
