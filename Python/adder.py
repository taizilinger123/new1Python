#!/usr/bin/env python
# encoding: utf-8
'''
@author: sige
@license: (C) Copyright 2018-2020.
@contact: 837337164@qq.com
@software: pycharm
@file: adder.py
@time: 8/20/2018 4:08 PM
@desc: this is a test python script
'''
import sys
sum = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        sum += int(line)
print(sum)