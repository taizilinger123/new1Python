#!/usr/bin/env python
# encoding: utf-8
'''
@author: sige
@license: (C) Copyright 2018-2020.
@contact: 837337164@qq.com
@software: pycharm
@file: sorter.py
@time: 8/20/2018 4:07 PM
@desc: this is a test python script
'''
import sys
lines = sys.stdin.readlines()
lines.sort()
for line in lines:print(line, end='')