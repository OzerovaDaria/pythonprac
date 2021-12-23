def f(d, N, c):
    for i in c:
        if N == len(i):
            d.setdefault(i.lower(), 0)
            d[i.lower()] += 1
    return d
    
N = int(input())
d = {}
c = ["."]
while (s := input()):
    # print(s)
    for i in s:
        if not i.isalpha():
            s = s.replace(i, ' ')
    c = s.split()
    d = f(d, N, c)
print(" ".join([i for i in d if d[i]==d[max(d, key=d.get)]]))
