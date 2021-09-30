#print([i for i in range (0, 100, 2) if '3' not in str(i)]) - упражнение
b, e = eval(input())
print([i for i in range(b if b > 1 else 2, e) if all([i % k for k in range(2, int(i ** 0.5) + 1)])])

