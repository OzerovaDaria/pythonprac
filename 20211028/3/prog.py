import itertools

"""
print(list(itertools.product("qwer", "123")))
print(list(itertools.permutations("qwer", 2)))
"""

print(*sorted(filter(lambda x: x.count("TOR") == 2 , map(lambda x: "".join(x).replace('*', 'TOR') , itertools.product('TOR*', repeat = int(input()) - 4))))) 

