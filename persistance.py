# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 16:28:05 2017

@author: eria
"""

def persistence(n):
    persist = 0
    string_n = str(n)
    while len(string_n) > 1:
        new_num = 1
        persist += 1
        for digit in string_n:
            new_num = new_num * int(digit)
        string_n = str(new_num)
    return(persist)
    