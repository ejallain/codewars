# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:25:04 2017

@author: eria
"""


def convert(in_put, source, target):
    source_base = len(source)
    target_base = len(target)
    source_dict = {x:i for i, x in enumerate(source)}
    target_dict = {i:x for i, x in enumerate(target)}
    dec_num = 0
    for i, digit in enumerate(in_put[::-1]):
        dec_num = dec_num + source_dict[digit] *  source_base**i
    print("Dec Num: ", dec_num)
    div, rem = divmod(dec_num, target_base)
    output = target_dict[rem]
    print(output[::-1])
    while div >= target_base:
        div, rem = divmod(div, target_base)
        output = output + target_dict[rem]
    if div != 0:
        output = output + target_dict[div]
    return(output[::-1])
        