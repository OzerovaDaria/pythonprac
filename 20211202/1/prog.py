class dump(type):
    def __init__(cls, clsname, parents, namespace):
        for (n, f) in namespace.items():
            if callable(f): 
                def partial(foo, name):
                    def wrap(self, *args, **kwargs):
                        print(f'{name}: {args}, {kwargs}')
                        return foo(self, *args, **kwargs)
                    return wrap
            else:
                continue
            setattr(cls, n, partial(f, n))


import sys
exec(sys.stdin.read())
