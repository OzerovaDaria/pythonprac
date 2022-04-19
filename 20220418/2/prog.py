class SquareIO():

    def __init__(self):
        return

    def inputCoeff(self, name):
        return input(f"Input {name}: ")

    def printResult(self, result):
        print(f"Solution: {result}")

def my_print(str):
    SquareIO().printResult(str)

def solveSquare(a, b, c):
    if a != 0:
        d = b ** 2 - 4 * a * c
        if d >= 0:
            d = d ** 0.5
            x1 = (- b - d) / (2 * a)
            x2 = (- b + d) / (2 * a)
            return (x1, x2)
        else:
            my_print("нет решений x")
            return None
    else:
        if b == 0:
            if c != 0:
                my_print("нет решений x")
                return None
            else:
                my_print("x принадлежит (-inf, +inf)")
                return None
        else:
            return (-c / b, -c / b)


def my_solve():
    a = float(SquareIO().inputCoeff('a'))
    b = float(SquareIO().inputCoeff('b'))
    c = float(SquareIO().inputCoeff('c'))
    res = solveSquare(a, b, c)
    if res:
        SquareIO().printResult(res)

if __name__ == "__main__":
    my_solve()


