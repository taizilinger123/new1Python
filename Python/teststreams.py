#!/usr/bin/env python
# encoding: utf-8
'''
@author: sige
@license: (C) Copyright 2018-2020, Node Supply Chain Manager Corporation Limited.
@contact: 837337164@qq.com
@software: garner
@file: teststreams.py
@time: 8/20/2018 3:25 PM
@desc:
'''
def interact():
    print('Hello stream world')
    while True:
        try:
            reply = input('Enter a number>')
        except EOFError:
            break
        else:
            num = int(reply)
        print("%d squared is %d" % (num, num ** 2))
    print('Bye')
if __name__ == '__main__':
    interact()