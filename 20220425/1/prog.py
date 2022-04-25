import gettext
from pyfiglet import figlet_format


def solve(a, b):
    return None if a == 0 else (-b/a)

if __name__ == '__main__':
    translation = gettext.translation("prog", "po", fallback=True)
    _ = translation.gettext 
    result = solve(float(input()), float(input()))
    if result != None:
        r = _('Root: {}')
        print(figlet_format(r.format(result)))
    else:
        r = _('NO ROOTS')
        print(figlet_format(r))
