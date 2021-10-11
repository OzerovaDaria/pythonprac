def Pareto (m):  
    return (tuple([(x, y) for x, y in m if all([not(x <= a and y <= b and (x < a or y < b)) for a, b in m])]))
m = eval(input())
print(Pareto(m))
