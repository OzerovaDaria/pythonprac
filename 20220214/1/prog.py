#!/usr/bin/python3
'''
'''
import sys
import zlib
from os.path import basename, dirname
import os

pr = '../../.git'
pr += "/refs/heads"
if len(sys.argv) == 1:
    for store in os.listdir(pr):
        print(store)
