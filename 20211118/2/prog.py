class Num:
    def __get__(self, obj, cls):
        print(f"Get from {cls}:{obj}")
        return obj._value

    def __set__(self, obj, val):
        if val.isdigit():
             obj._value = val
        else:
            obj._value = len(val)
        print(f"Set in {obj} to {val}")
       

    def __delete__(self, obj):
        print(f"Delete from {obj}")
        obj._value = None

class C:
    num = Num()

print(C().num)
c, d = C(), C()
c.num = d.num = 2
print(c.num+d.num)
c.num = "qwerqwerqwer"
print(c.num+d.num)
d.num = range(10, 1000, 7)
print(c.num+d.num)
