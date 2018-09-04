#!/usr/bin/env python
# encoding: utf-8
'''
@author: sige
@license: (C) Copyright 2018-2020.
@contact: 837337164@qq.com
@software: pycharm
@file: more.py
@time: 8/20/2018 4:37 PM
@desc: this is a test python script
'''
def more(text, numlines=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:print(line)
        if lines and input('More?') not in ['y', 'Y']:break
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())