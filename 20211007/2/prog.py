def SUB(a, b):
    if type(a) is tuple: return tuple(x for x in a if all([x != y for y in b]))
    elif type(a) is list : return list(x for x in a if all([x != y for y in b]))
    elif str(a).isnumeric: return a-b
    
a, b = eval(input())
print(SUB(a, b))
