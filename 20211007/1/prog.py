def Pareto (*m):
    return ([(x, y) for x, y in m if all([x >= a and y >= b and (x > a or y > b) for a, b in m])])

print(Pareto((1,2), (3,4), (2,2), (4,3), (7,0), (1,8), (88, 88)))
