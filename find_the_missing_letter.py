# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 09:25:05 2017

@author: eria
"""

def find_missing_letter(chars):
    return([chr(ord(c)-1) for i,c in enumerate(chars) if ord(c) != ord(chars[0])+i][0])