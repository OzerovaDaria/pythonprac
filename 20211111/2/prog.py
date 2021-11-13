def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def triangleSquare(x1, y1, x2, y2, x3, y3):
    a = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    b = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    c = ((x3 - x1)**2 + (y3 - y1)**2)**0.5
    if a + b > c and a + c > b and b + c > a:
    #print(a, b, c)
        p = (a + b + c) / 2.0 
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(toFixed(S, 2))
    else:
        raise BadTriangle()
    
class InvalidInput:

class BadTriangle(Exception):
    pass
    


instr = input()
try:
    (x1, y1), (x2, y2), (x3, y3) = eval(instr)
except Exception:
    print(Invalid input)
print((x1, y1), (x2, y2), (x3, y3))
triangleSquare(x1, y1, x2, y2, x3, y3)
