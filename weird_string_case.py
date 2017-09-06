# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 13:10:29 2017

@author: eria
"""


def to_weird_case(string):
    words = string.split()
    weird_string = []
    for n, word in enumerate(words):
        weird_string.append('')
        for i,letter in enumerate(word):
            if i % 2 == 0:
                weird_string[n] = weird_string[n] + letter.upper()
            else:
                weird_string[n] = weird_string[n] + letter.lower()
    return(' '.join(weird_string))
            
        
        
    