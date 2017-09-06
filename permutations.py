# -*- coding: utf-8 -*-
"""
Created on Sat May  6 06:50:01 2017

@author: eria
"""

import itertools


def permutations(string):
    return(list({''.join(x) for x in itertools.permutations(string)}))
