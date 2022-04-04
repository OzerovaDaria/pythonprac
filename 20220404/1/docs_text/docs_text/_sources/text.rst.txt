=================
Суть проекта
=================

Старый добрый сапер

Ссылка на репозиторий:
`<https://github.com/OzerovaDaria/py_project>`_

=================
Участники
=================
* Панферов Виктор, 321
* Озерова Дарья, 321
* Андрей Казаринов, 316


=================
Пример кода
=================
::

    def cellInfo(self, x, y=None):
        """Get cell draw character and color used."""
        if y is None:
            cell = self.field[Point(x)]
        else:
            cell = self.field[Point(x, y)]

        if cell == Mask.closed:
            if cell == Flag.noflag:
                return ' ', Color.bg.grey
            elif cell == Flag.guess:
                return 'G', Color('yellow', 'grey')
            elif cell == Flag.sure:
                return 'F', Color('banana', 'grey')
        else:
            if cell == Value.bomb:
                return '*', Color.red
            elif cell == Value.empty:
                return ' ', Color.white
            else:
                return str(cell), Color(VALUECOLORS[cell.value])
