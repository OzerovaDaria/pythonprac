def my_print(not_waterr, val, waterr):
    print('.' * not_waterr   + ' ' * (val - not_waterr)   + f' {not_waterr}/{total}')
    print('~' * waterr + ' ' * (val - waterr) + f' {waterr}/{total}')

fline = input()
waterr, h = 0, 0
not_waterr = 0
w = len(fline) - 2
while True:
    line = input()
    not_waterr   += line.count('.')
    waterr += line.count('~')
    h += 1
    if (fline == line): break
w, h = h, w
print('#' * w + '##')
for i in range(h):
    print('#', end='')
    if not_waterr - i * w > 0:
        print('.' * w, end='')
    else:
        print('~' * w, end='')
    print('#')
print('#' * w + '##')
val = max(waterr, not_waterr)
total = not_waterr + waterr
my_print(not_waterr, val, waterr)
