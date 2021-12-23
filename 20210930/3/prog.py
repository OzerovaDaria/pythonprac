raw = []
try:
    s = input()
    while s != '':
        raw.append([int(i) for i in s.split(',')])
        s = input()
except:
    pass        
A = raw[:len(raw) // 2]
B = raw[len(raw) // 2 :] 
result = a = [[0] * len(A[0]) for i in range(len(A[0]))]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j] 
for row in result:
    print(row)
import sys
exec(sys.stdin.read())
