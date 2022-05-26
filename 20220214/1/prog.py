import sys
import os
import zlib

def my_print(lvl, tname, modl, num):
    print(f"{SHIFT * lvl}{tname.decode()} {modl.decode()} {num.hex()}")

def print_tree(repo, fd, lev=0):
    opath = os.path.join(repo, ".git", "objects", fd[0:2], fd[2:])
    with open(opath, "rb") as ofile:
        header, a, body = zlib.decompress(ofile.read()).partition(b"\x00")
        next, a = header.split()
    a, end = next, body
    while end:
        trtr, a, end = end.partition(b"\x00")
        num, end = end[:20], end[20:]
        modl, tname = trtr.split()
        my_print(lev, tname, modl, num)
        if modl == b"40000":
            print_tree(repo, num.hex(), lev+1)

def print_branches():
    print(" ".join(os.listdir(branches)))

SHIFT = "  "
repo = os.path.join("..", "..")
branches = os.path.join(repo, ".git", "refs", "heads")

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print_branches()
    else:
        bpath = os.path.join(branches, sys.argv[1])
        with open(bpath, "r") as f:
            nst = f.read().strip()
        while True:
            try:
                opath = os.path.join(repo, ".git", "objects", nst[0:2], nst[2:])
                with open(opath, "rb") as ofile:
                    header, a, body = zlib.decompress(ofile.read()).partition(b"\x00")
                    next, a = header.split()
                a, commit_body = next, body
                extra = commit_body.decode()
                print("| commit:", nst)
                print(extra)
                extra = extra.split()
                tr = extra[extra.index('tree') + 1]
                print_tree(repo, tr)
                if 'parent' not in extra:
                    break

                print('\n')
            except:
                break
