#!/usr/bin/python3
'''
'''
import sys
from zlib import decompress
import zlib
import os
from os.path import basename, dirname

def find_parent(body):
    it = iter(body.decode().split('\n'))
    while iter:
        st = next(it)
        if not st:
            break
        m = st.split(" ", 1)
        if m[0] == 'parent':
            return m[1]

def body_format(body):
    r = []
    while body:
        h, a, l = body.partition(b'\x00')
        body = l[20:]
        g = l[:20]
        gh = g.hex()
        hd = h.decode()
        r.append(f'{hd} {gh}')
    return '\n'.join(r)

def pass_tree(pr, tree_obj, st):
    #print(st)
    while 1:
        f = open(tree_obj, 'rb')
        obj = zlib.decompress(f.read())
        h, c, body = obj.partition(b'\x00')
        body_copy = body
        a, size = h.split()
        f.close()
        a, b = a.decode(), int(size)
        print('|', "type", a, '\n| size', b)
        if a != 'tree':
            break
        body01 = body_format(body_copy)
        if (body01 != None ):
            for i in body01.split('\n'):
                print('| ', i[0:], sep='')
        tree_next = body.partition(b'\x00')[2][:20].hex()
        tree_obj = os.path.join(pr, tree_next[:2], tree_next[2:])
        print('|', '*'*20)
        print("|")


pr = '../../.git'
if len(sys.argv) == 1:
    pr += "/refs/heads"
    for store in os.listdir(pr):
        print(store)
elif len(sys.argv) > 1:
    #if sys.argv[2] == 'last':
    f = open(os.path.join(pr + "/refs/heads", sys.argv[1]), 'r')
    num = f.readline()[:-1]
    pr += '/objects'
    last_commit = os.path.join(pr, num[0:2], num[2:])
    f.close()
    f = open(last_commit, 'rb')
    obj = decompress(f.read())
    h, a, body = obj.partition(b'\x00')
    a, size = h.split()
    f.close()
    print('last commit in', sys.argv[1], "branch ", ''.join(last_commit.split('/')[-2:]), "\nsize", int(size))
    print(body.decode())



    str_tree, a, b = body.partition(b'\x00')
    st = str_tree.decode().split(' ')[1][:40]
    #print(str_tree.decode().split(' '))
    tree_obj = os.path.join(pr, st[0:2], st[2:])
    pass_tree(pr, tree_obj, str_tree.decode().split(' '))

    parent = find_parent(body)
    print("PARENT", parent)
    while (parent):
        print("PARENT", parent)
        num = parent
        pr += '/objects'
        last_commit = os.path.join(pr, num[0:2], num[2:])
        print("LAST", last_commit)
        try:
            f = open(last_commit, 'rb')
        except FileNotFoundError as e:
            print("fail")
            break
        obj = decompress(f.read())
        h, a, body = obj.partition(b'\x00')
        a, size = h.split()
        f.close()
        print('next commit', ''.join(last_commit.split('/')[-2:]), "\nsize", int(size))
        print(body.decode())
        parent = find_parent(body)
        try:
            str_tree, a, b = body.partition(b'\x00')
            st = str_tree.decode().split(' ')[1][:40]
            # print(str_tree.decode().split(' '))
            tree_obj = os.path.join(pr, st[0:2], st[2:])
            pass_tree(pr, tree_obj, str_tree.decode().split(' '))
        except FileNotFoundError as e:
            pass










