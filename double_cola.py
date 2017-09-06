# -*- coding: utf-8 -*-
"""
Created on Fri May  5 05:12:04 2017

@author: eria
"""


def whoisnext_slow(names_list, n):
    while n > 0:
        names_list.append(names_list[0])
        names_list.append(names_list[0])
        name = names_list.pop(0)
        n = n - 1
    return(name)


def whoIsNext(names, r):
    if r == 0:
        return(names[0])
    cycles = 0
    list_len = orig_list_len = len(names)
    while list_len < r:
        list_len = orig_list_len + list_len * 2
        cycles += 1
    i = orig_list_len - 1 - ((list_len -r) // (2**cycles))
    return(names[i])

 def num_cycles(list_len, n):
    cycles = 0
    orig_list_len = list_len
    while list_len < n:
        list_len = orig_list_len + list_len * 2
        cycles += 1
    print("Cycles: ", cycles)
    print("List length: ", list_len)
    print("Remainder: ", list_len -n)
    print("Position: ", orig_list_len - 1 - ((list_len -n) // (2**cycles)))
    return(cycles)

