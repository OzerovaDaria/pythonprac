a = int(input())
if a % 25 == 0:
    if a % 2 == 0:
        print("A+ ")
        print("B- ")
    else:
        print("A- ")
        print("B+ ")
else:
    print("A- ")
    print("B- ")
if a % 8 == 0:
    print("C+")
else:
    print("C-")
