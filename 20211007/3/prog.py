def Bisect(x, s):
    if list(s) != sorted(s): return False
    n = len(s)//2
    if n == 0:
        if x == s[n]: return True
        else: return False
    else:
        if x < s[n]: return Bisect(x, s[:n])
        else: return Bisect(x, s[n:])
a, b = eval(input())
print(Bisect(a, b))

