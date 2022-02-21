import ipsedixit
from sys import argv

count = len(argv)

def my_print(m, n):
    g = ipsedixit.Generator(m)
    par = g.paragraphs(n)
    for p in par:
        print(p, end='\n\n')

mes = ''
if count == 1:
    mes = ipsedixit.Generator()
else:
    mes = 'tacitus'
    if count == 3:
        if argv[2] != 'caesar':
            if argv[2] != 'tacitus':
                f = open(argv[2], 'r')
                mes = f.read()
                f.close()
    my_print(mes, int(argv[1]))

