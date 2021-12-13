class check(type):
    def __init__(cls, cls_name, parents, ns):
        def checkit(self):
            for (n, _type) in self.__annotations__.items():
                my_aatr = getattr(self, n, None)
                if not isinstance(my_aatr, _type):
                    return False
            return True
        cls.check_annotations = checkit


import sys
exec(sys.stdin.read())
