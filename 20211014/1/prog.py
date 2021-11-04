import fractions
str = input().split(", ")
m = []
for i in str:
    m.append(fractions.Fraction(i))
res = 0
sum = 0
i = 3
grade = m[2]
while (grade >=0):
    sum += m[0]**(grade)* m[i]
    i += 1
    grade -= 1
i += 1
grade = m[i-1]
while (grade >=0):
    res += m[0]**(grade)* m[i]
    i += 1
    grade -= 1
if res != 0:
    if (sum / res == m[1]):
        print('True')
    else:
        print('False')
else: print('False')
