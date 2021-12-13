#prog3
import sys
st = sys.stdin.buffer.read()
a = int.from_bytes(st[4:8],   'little')
b = int.from_bytes(st[20:22], 'little')
c = int.from_bytes(st[22:24], 'little')
d = int.from_bytes(st[24:28], 'little')
e = int.from_bytes(st[34:36], 'little')
f = int.from_bytes(st[40:44], 'little')
print(f'Size={a}, Type={b}, Channels={c}, Rate={d}, Bits={e}, Data size={f}')
