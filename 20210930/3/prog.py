str = input()
if str.isnumeric(): print(int(str)*int(input()))
else:
    a = [eval(str)]
    b = []
    size = len(eval(str))
    for i in range(1,size):
        a.append(eval(input()))
    for i in range(size):
        b.append(eval(input()))
    res = [[0]*size for i in range(size)]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                res[k][i] += int(a[k][j]) * int(b[j][i])
    for i in res:
        print(i)
