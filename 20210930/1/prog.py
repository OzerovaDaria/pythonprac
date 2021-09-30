lst = eval(input())
lst = list(lst)
for i in range(len(lst)-1):
    for j in range(len(lst)-1, i, -1):
        if (lst[j-1]**2)%100 > (lst[j]**2)%100:
            lst[j-1], lst[j] = lst[j], lst[j-1]
print(lst)
