import itertools
"""
print(list(intertools.repeat(42, 5)))
"""

def slide(seq, n):
    for i in range(n + 1):
        yield from itertools.islice(seq, i, i+n)
import sys
exec(sys.stdin.read())
    
