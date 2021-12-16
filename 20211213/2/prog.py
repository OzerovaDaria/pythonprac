import asyncio
from collections import defaultdict

async def merge(b0, e0, b1, e1, el, er, event):
    if b1 - b0 != 1:
        await el.wait()
        await er.wait()
    begin, i = b0, b0
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    await asyncio.sleep(0)
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[begin:e1] = LL[begin:e1]
    event.set()

async def joiner():
    d = defaultdict(asyncio.Event)
    st = 2
    m, n = [], 0
    while st <= 2 * len(L):
        for i in range(0, len(L), st):
            lb, le = i, i + st // 2
            rr = le
            re = min(i + st, len(L))
            if le >= len(L):
                d[(i, len(L))].set()
                continue
            el = d[(lb, le)]
            er = d[(rr, re)]
            if st == 2:
                el.set()
                er.set()
            event = d[(lb, re)]
            m.append(asyncio.create_task(merge(lb, le, rr, re, el, er, event)))
        st *= 2
    await asyncio.gather(*m)
L = eval(input())
LL = [0] * len(L)
asyncio.run(joiner())
print(L)
