st = input()
d = set()
j = 0
result = 0
size = len(st) - 1
while j != size:
    d.add((st[j] + st[j+1]).lower())
    j += 1
for i in d:
    if i.isalpha():
        result += 1
print(result)


"""
c = {}
for w in input().split():
    c[w] = c.setdefault(w, 0) + 1
    
"""
"""
if w in c:
        c[w] += 1
    else:
        c[w] = 1
"""
"""
import collections
collections.Counter("chbs ckdjk  clkwld".split())
"""
