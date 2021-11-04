import fractions
def make(m, grade):
    sum = 0
    res = 0
    i = 3
    while (grade >=0):
        sum += m[0]**(grade)* m[i]
        i += 1
        grade -= 1
    i += 1
    grade = m[i-1]
    while (grade >=0):
        sum += m[0]**(grade)* m[i]
        i += 1
        grade -= 1
    if res != 0:
        return(sum / res == m[1])
    else: return(False)

str = input().split(", ")
m = []
for i in str:
    m.append(fractions.Fraction(i))
if make(m, m[2]):
    print("True")
else:
    print("False")


