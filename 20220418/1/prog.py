def solveSquare(a, b, c):
    d = b**2 - 4 * a * c
    if d >= 0:
        d = d**0.5
        x1 = (- b - d) / (2 * a)
        x2 = (- b + d) / (2 * a)
        return (x1, x2)
    else:
        return None

