#a = input()
#print({c : c for c in a.split()})

import math

print(eval("x", {"x": 1}, math))

d = {}
st = input().split()
while st[0] != "quit":
    if st[0][0] == ":":
        d[st[0][1:]] = (st[2], st[1]) 
    st = input().split()

print(d)
