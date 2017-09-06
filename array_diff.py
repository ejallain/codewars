# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:28:26 2017

@author: eria
"""

def array_diff(a, b):
    return([i for i in a if i not in b])



print(array_diff([1,2],[1]), "a was [1,2], b was [1], expected [2]")
print(array_diff([1,2,2],[1]), "a was [1,2,2], b was [1], expected [2,2]")
print(array_diff([1,2,2],[2]), "a was [1,2,2], b was [2], expected [1]")
print(array_diff([1,2,2],[]), "a was [1,2,2], b was [], expected [1,2,2]")
print(array_diff([], [1,2]), "a was [], b was [1,2], expected []")