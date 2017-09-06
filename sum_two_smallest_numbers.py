# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:13:59 2017

@author: eria
"""


def sum_two_smallest_numbers(numbers):
    sorted_numbers = [num for num in sorted(numbers) if num > -1]
    return(sum(sorted_numbers[:2]))


print(sum_two_smallest_numbers([5,6,-2,3,1]))