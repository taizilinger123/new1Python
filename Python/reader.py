#!/usr/bin/env python
# encoding: utf-8
'''
@author: sige
@license: (C) Copyright 2018-2020.
@contact: 837337164@qq.com
@software: pycharm
@file: reader.py
@time: 8/20/2018 4:01 PM
@desc: this is a test python script
'''
print('Got this: "%s"' % input())
import sys
data = sys.stdin.readline()[:-1]
print('The meaning of life is', data, int(data)*2)