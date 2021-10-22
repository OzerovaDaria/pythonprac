import collections

def check(st):
    for i in st:
        if not (i.isalpha() or (i == '\t' or i == '\n')):
            st = st.replace(i, ' ')
    #print("st = ", st)
    return st

w = int(input())
d = {}
strstr = ''
st = input()
while True:
    if st == '': break
    strstr += check(st)
    st = input()
#print(strstr)
strstr = strstr.lower().split()
c = collections.Counter(strstr)
for key, i in c.items():
    if len(key) == w:
        d[key] = i
#print(c)
#print(d)
maxm = 0
if d:
    for i, j in d.items():
        if j > maxm:
            maxm = j
    for i in sorted([j for j in d if d[j] == maxm]):
        print(i, end=' ')
