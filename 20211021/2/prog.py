import math

d = {}
st = input().split()
while st[0] != "quit":
    #print(st)
    if st[0][0] == ":":
        key = st[0][1:]
        d[key] = [st[1], st[2]]
    else:
         print(eval(d[st[0]][1], {d[st[0]][0]: eval(st[1])}, math.__dict__))
    st = input().split()
#print(d)
print(len(d) + 1)
