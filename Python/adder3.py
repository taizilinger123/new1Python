#!/usr/bin/env python
# encoding: utf-8
'''
@author: sige
@license: (C) Copyright 2018-2020.
@contact: 837337164@qq.com
@software: pycharm
@file: adder3.py
@time: 8/20/2018 4:27 PM
@desc: this is a test python script
'''
import  sys
sum  = 0
for line in sys.stdin: sum += int(line)
print(sum)