def myprint(gas, p, water):
    print('.' * gas   + ' ' * (p - gas)   + f' {gas}/{res}')
    print('~' * water + ' ' * (p - water) + f' {water}/{res}')
fline = input()

water = 0
gas = 0
ww = len(fline) - 2
hh = 0

while True:
    line = input()
    gas   += line.count('.')
    water += line.count('~')
    hh += 1
    if (fline == line): break
hh -= 1

ww, hh = hh, ww
print('#' * ww + '##')
for i in range(hh):
    print('#', end='')
    if gas - i * ww > 0:
        print('.' * ww, end='')
    else:
        print('~' * ww, end='')
    print('#')
print('#' * ww + '##')
p = max(water, gas)
res = gas + water
myprint(gas, p, water)

