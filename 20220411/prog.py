import gettext

translation = gettext.translation('tra', "po", fallback=True)
_, ngettext = translation.gettext , translation.ngettext

'''
def dialog():
    while s := input(_("Input string: ")):
        print(_("{} and what?").format(s))

'''
def dialog():
    while s:= input(_("Input string: ")):
        n = len(s.split())
        print(ngettext("{} word entered", "{} words entered", n).format(n))


if __name__ == "__main__":
    dialog()
