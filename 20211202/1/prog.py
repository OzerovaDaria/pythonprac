class dump(type):
    def __init__(cls, n, parents, space):
        for (n, f) in space.items():
            if callable(f): 
                def pp(foo, nm):
                    def wrap(self, *args, **kwargs):
                        per = f'{nm}: {args}, {kwargs}'
                        print(per)
                        return foo(self, *args, **kwargs)
                    return wrap
            else:
                continue
            setattr(cls, n, pp(f, n))


import sys
exec(sys.stdin.read())
