"""import strystr

def strep(m):
  llen = m[0:1][0]
  text = m[1:]
  return len(text) // llen + 1 if  len(txt) % llen else len(text) // llen

def my_write(a, text):
  sys.stdout.buffer.write(bytestr(text[0:1]))
  for i in a:
    sys.stdout.buffer.write(bytestr(i))
    
#ch = sys.stdin.buffer.read(1)
ch_mastr= bytearray(sys.stdin.buffer.read())
str= sep(ch_mastr)
f = []
text = ch_mas[1:]
for i in range(ch_mas[0:1][0]):
  f.append(text[i*s:(i+1)*s])
f = sorted(f)
my_write(f,ch_mas[0:1][0])

"""
def f (n, l, st, res):
    mas = []
    for i in range(n):
        mas.append(st[i*l//n:(i+1)*l//n])
    mas.sort()
    for i in mas:
        res += i
    return res
        
import sys

s = sys.stdin.buffer.read()
n = s[0]
result = s[0:1]
s = s[1:]
result = f(n, len(s) - 1, s, result)
sys.stdout.buffer.write(result)
