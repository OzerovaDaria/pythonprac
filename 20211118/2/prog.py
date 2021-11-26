class Num:
    def __get__(self, obj, cls):
        #print(f"Get from {cls}:{obj}")
        return getattr(obj, "_val", 0)

    def __set__(self, obj, val):
        if hasattr(val, "real"):
             obj._val = val
        else:
            obj._val = len(val)
        #print(f"Set in {obj} to {val}")
       
    def __delete__(self, obj):
        #print(f"Delete from {obj}")
        obj._val = None

import sys
exec(sys.stdin.read())


