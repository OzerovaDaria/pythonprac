str = eval(input())
str = list(str)
for i in range(len(str)-1):
    for j in range(len(str) - i - 1):
        if (str[j]**2 % 100) > (str[j+1]**2 % 100):
            str[j+1], str[j] = str[j], str[j+1]
print(str)
