import cmd
import shlex

class Monster(cmd.Cmd):

    def __init__(self):
        super(Monster, self).__init__()
        self.vec = ['up', 'down', 'left', 'right']
        self.player01 = 0
        self.player02 = 0
        self.monsters = []

    def print_first_argument(self):
        print("Please, type monster")

    def print_player(self, args):
        print(f'your player is at {self.player01} {self.player02}')

    def print_cords(self, n, cordx, cordy, hp):
        print(f'{n} at ({cordx} {cordy}) hp {hp}')

    def next_print(self, n, i):
        print(f'{n} lost 10 hp, now has {i} hp')

    def check (self, args):
        if args[0] != "monster" or args[1] != "name":
            self.print_first_argument()
            return True
        if args[3] != "hp" or args[5] != "coords":
            self.print_first_argument()
            return True
        return False

    def parse (self, args):
        hp = int(args[4])
        name = args[2]
        cordx, cordy = int(args[6]), int(args[7])
        monsters_info = [cordx, cordy, name, hp]
        self.monsters.append(monsters_info)

    def do_add(self, args):
        args = shlex.split(args)
        if len(args) != 8:
            print("Wrong count of arguments")
            return
        elif self.check(args):
            return
        else:
            self.parse(args)

    def init_monster (self):
        for i in self.monsters:
            cordx, cordy = i[0], i[1]
            name, hp = i[2], i[3]
            self.print_cords(name, cordx, cordy, hp)

    def do_show(self, args):
        args = shlex.split(args)
        if len(args) != 1:
            self.print_first_argument()
            return
        elif args[0] != "monsters":
            self.print_first_argument()
            return
        else:
            self.init_monster()

    def complete_show(self, start):
        return [i for i in ["monsters", ] if i.startswith(start)]

    def direction (self, args):
        arg1 = 0
        arg2 = 0
        if args[0] == "right" or args[0] == "down":
            arg1, arg2 = 9, 1
        elif args[0] == "up" or args[0] == "left":
            arg1, arg2 = 0, -1

        if args[0] == "up" or args[0] == "down":
            if self.player01 == arg1:
                return
            else:
                self.player01 += arg2
        else:
            if self.player02 == arg1:
                return
            else:
                self.player02 += arg2

    def do_move(self, args):
        args = shlex.split(args)
        if len(args) != 1:
            self.print_first_argument()
            return
        elif args[0] not in self.vec:
            print("Choose direction from : up, down, left, right")
            return
        else:
            str = "encountered: "
            fl1, fl2 = 0, 0
            self.direction(args)
            self.print_player(args)
            for i in self.monsters:
                if i[0] == self.player01:
                    if i[1] == self.player02:
                        fl1 = 1
                        if fl2:
                            fl2 = 1
                            str += ", "
                        str += i[2] + " " + str(i[3]) + " hp"
            if fl1:
                print(str)

    def complete_move(self, start):
        return [i for i in self.vec if i.startswith(start)]

    def do_attack(self, args):
        args = shlex.split(args, comments=True)
        if len(args) < 1:
            print("cant move")
            return
        elif len(args) > 1:
            print("cant move, please, add argument")
            return
        else:
            pl_name = args[0]
            fl = 1
            for i in self.monsters:
                if i[0] == self.player01 and i[1] == self.player02:
                    if pl_name == i[2]:
                        i[3] -= 10
                        self.next_print(pl_name, i[3])
                        fl = 0
                        if i[3] <= 0:
                            print(f'{pl_name} dies')
                            self.monsters.remove(i)

    def complete_attack(self, start):
        dct = {}
        ind = 0
        for m in self.monsters:
            if m[1] == self.player02:
                if m[0] == self.player01:
                    dct[ind] = m[2]
                    ind += 1
        mn = [i for i in dct.values() if i.startswith(start)]
        return mn

    def do_exit(self, args):
        return True

Monster().cmdloop()