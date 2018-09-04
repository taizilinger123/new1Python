#!/usr/bin/env python
# encoding: utf-8
'''
@author: sige
@license: (C) Copyright 2018-2020.
@contact: 837337164@qq.com
@software: pycharm
@file: redirect.py
@time: 8/21/2018 11:06 AM
@desc: this is a test python script
'''
import  sys

class Output:
    def __init__(self):
        self.text = ''
    def write(self, string):
        self.text += string
    def writelines(self, lines):
        for line  in lines: self.write(line)
class Input:
    def __init__(self, input=''):
        self.text = input
    def read(self, size=None):
        if size == None:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:size], self.text[size:]
        return res
def readline(self):
    eoln = self.text.find('\n')
    if eoln == -1:
        res, self.text = self.text, ''
    else:
        res, self.text = self.text[:eoln+1], self.text[eoln+1:]
    return res
def  redirect(function, pargs, kargs, input):
    savestreams = sys.stdin, sys.stdout
    sys.stdin = Input(input)
    sys.stdout = Output()
    try:
        result = function(*pargs, **kargs)
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams
        return (result, output)


