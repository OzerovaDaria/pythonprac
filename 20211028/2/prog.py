import itertools
"""
print(list(intertools.repeat(42, 5)))
"""
import sys

def slide(seq, n):
    s = seq
    while True:
        seq = iter(seq)
        s, seq = itertools.tee(s)
        w = list(itertools.islice(seq, n))
        if len(w) < 1:
            return
        yield from w
        next(s)
exec(sys.stdin.read())

