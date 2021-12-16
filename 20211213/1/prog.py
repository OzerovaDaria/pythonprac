#!/usr/bin/env/ python3
'''
'''
import random
import asyncio
L = list(range(16))
random.shuffle(L)
LL = L.copy()

# [1, 2, 3, 4, [7, 8] ... ]
async def merge(b0, b1, e1, el, er, ee):
    if b1 != b0 + 1:
        await el.wait()
        await er.wait()
    b, e0, i = b0, b1, b0
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    ee.set()

async def joiner():
    m = []
    j = 0
    d = {}
    for p in range(4):
        b = 2**(p + 1)
        for i in range(0, len(L), b):
            par = i+b
            d[(i, par)] = asyncio.Event()
            if b == 2:
                el, er = None, None
            else:
                el, er = d[(i, i+b//2)], d[(i+b//2, par)]
            event = d[(i, par)]
            #await merge(i, i + b // 2, i + b)
            m.append(asyncio.create_task(merge(i, i + b // 2, par ,el ,er ,event)))
    await asyncio.gather(*m)

L = eval(input())
asyncio.run(joiner())
print(L)
