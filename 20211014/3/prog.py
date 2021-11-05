def my_scanf(m):
    str =  input()
    if len(str)==0:
        return []
    str = input()
    while str[1] != "#":
        lst = []
        for i in range(1, len(str)):
            lst.append(str[i])
        m.append(lst)
        str = input()
    return m

def my_print(g, w, ww):
    for i in range(ww + 2):
        print("#", end = '')
    print()
    for i in range(g // ww):
        print("#" + "." * ww + "#", end = '\n')
    for i in range(w // ww):
        print("#" + "~" * ww + "#", end = '\n')
    for i in range(ww + 2):
        print("#", end = '')
    print()

w, g, n = 0, 0, 0
m = []
mas = my_scanf(m)
if len(mas) != 0:
    for i in mas: 
        w += i.count("~")
        g += i.count(".")
    hh, ww = len(mas), len(mas[0])
    n = hh
    hh = ww
    ww = n
    my_print(g, w, ww)
