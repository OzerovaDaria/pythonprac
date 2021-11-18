def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

class InvalidInput(TypeError):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(x1, y1, x2, y2, x3, y3):
    a = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    b = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    c = ((x3 - x1)**2 + (y3 - y1)**2)**0.5
    try:
        if not (a + b > c and a + c > b and b + c > a):
    #print(a, b, c)
            raise BadTriangle("Not a triangle")
    except BadTriangle:
        raise BadTriangle("Not a triangle")
    else:
        p = (a + b + c) / 2.0 
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        #print(toFixed(S, 2))
        return toFixed(S, 2)

sqt = 0
while True:
    try:
        instr = input()
        try:
            (x1, y1), (x2, y2), (x3, y3) = eval(instr)
        except Exception:
            raise InvalidInput("InvalidInput")
        #print((x1, y1), (x2, y2), (x3, y3))
        sqt = triangleSquare(x1, y1, x2, y2, x3, y3)
    except InvalidInput as II:
        print(II)
    except BadTriangle as BT:
        print(BT)
    else:
        print(sqt)
        break
