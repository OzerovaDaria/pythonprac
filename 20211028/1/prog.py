def fib(m, n):
    fib1, fib2 = 0, 1
    for i in range(m):
        fib1, fib2 = fib2, fib1+fib2
    for i in range(n - m + 1):
        fib1, fib2 = fib2, fib1+fib2
        yield fib1

m, n = eval(input())
for f in fib(m, n):
    print(f, end = ' ')
