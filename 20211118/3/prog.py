import string
class Alpha:
    __slots__ = [*string.ascii_lowercase]
    def __str__(self):
        a = ""
        for i in string.ascii_lowercase:
            if hasattr(self, i):
                a += f'{i}: {getattr(self, i)}, '
        return a[:-2]
    
    def __init__(self, **args):
        for i, j in args.items():
            setattr(self, i, j)
    

class AlphaQ:
    def __init__(self, **kwargs):
        for i, j in kwargs.items():
            if i in string.ascii_lowercase:
                setattr(self, i, j)
            else:
                raise AttributeError()
    
    def __str__(self):
        a = ""
        for i in string.ascii_lowercase:
            if hasattr(self, i):
                a += f'{i}: {getattr(self, i)}, '
        return a[:-2]
    
    def __getattr__(self, i):
        if i in dir(self):
            return self.i
        else:
            raise AttributeError()
        
    #def __del__():
        #pass
    #print()

import sys
exec(sys.stdin.read())

