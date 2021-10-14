def make_p(grade, n, *k):
    i = 0
    sum = 0
    while (grade >=0):
        sum += n**(grade)* k[i]
        i += 1
        grade -= 1
    return sum

s, w, a, *m = input().split(", ")
kA = []
kB = []
sA = int(a)
print(m)
for i in range(sA+1):
        kA.append(m[i])
sB = int(m[sA])
for j in range(sA+1, len(m)-1):
        kB.append(m[sB + j])
print(s, w, sA, sB)
print(kA)
print(kB)
print(make_p(sA, int(s), kA))
print(make_p(sB, int(s), kB))
