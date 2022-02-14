#!/usr/bin/python3
'''
'''
import sys
from zlib import decompress
import zlib
import os
from os.path import basename, dirname


pr = '../../.git'
if len(sys.argv) == 1:
    pr += "/refs/heads"
    for store in os.listdir(pr):
        print(store)
elif len(sys.argv) > 1:
    if sys.argv[2] == 'last':
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
        exit()



