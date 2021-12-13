class check(type):
    def __init__(cls, n, father, ns):
        def checkit(self):
            for (n, _type) in self.__annotations__.items():
                if isinstance(getattr(self, n, None), _type):
                    continue
                else:
                    return False
            return True
        cls.check_annotations = checkit


import sys
exec(sys.stdin.read())
