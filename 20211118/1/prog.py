"""
def dump(fn):
    def newf(*args, **kwargs):
        print("->", args, kwargs)
        res = fn(*args, **kwargs)
        print("<-", res)
        return res
    return newf

@dump
def fun(a, b):
    return a*2 + b
a, b = eval(input())
fun(a, b)

def iint(typ):
    def decor(fn):
        def fu(*args):
            if any(type(a) is not typ for a in args):
                raise TypeError("Not int")
            return fn(*args)
        return fun
    return decor

@iint(str)
def fun(a, b):
    return a*2 + b
a, b = eval(input())
fun(a, b)

def dumpc(cls):
    class newcl(cls):
        def __str__(self):
            res = super().__str__()
            return


"""
