# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 09:49:38 2017

@author: eria
"""


def unique_in_order(iterable):
    return([iterable[n] for n,_ in enumerate(iterable) if n == 0 or iterable[n-1] != iterable[n]])






print(unique_in_order('AAAABBBCCDAABBBACC'))
print(unique_in_order(''))
print(unique_in_order('A'))
