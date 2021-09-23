sum = 0
while a := int(input()):
    sum += a
    if sum > 21:
        print(sum)
        break
    elif a <= 0:
        print(a)
        break

