# values = eval(input())
import fractions
def pareto(cfs, v):
    s = fractions.Fraction(0)
    ind = 0
    for item in cfs:
        s += item * v ** (ind)
        ind += 1
    return s 
values = input().split(",")
s, w = fractions.Fraction(values[0]), fractions.Fraction(values[1])
nA = int(values[2])
nA += 1
A = [fractions.Fraction(item) for item in values[3 : 3 + nA]]
nB =int(values[3 + nA])
nB += 1    
B = [fractions.Fraction(item) for item in values[4 + nA : 4 + nA + nB]]
print(pareto(A[::-1], s) / pareto(B, s) == w)

