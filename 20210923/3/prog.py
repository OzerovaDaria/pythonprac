def sum_of_ch(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum
n = int(input())
i = j = n
while i != n+3:
    while j != n+3:
        if sum_of_ch(i*j) == 6:
            print (i,"*",j, "=", ":=)", sep='', end = " ")
        else:
            print (i,"*",j, "=", i * j, sep='', end = " ")
        j += 1
    j = n
    i += 1
    print('\n')
