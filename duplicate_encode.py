# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 09:06:52 2017

@author: eria
"""


def duplicate_encode(word):
    num_word = [word.lower().count(letter) for letter in word.lower()]
    encoded_word = [')' if num >1 else '(' for num in num_word]
    return(''.join(encoded_word))

print(duplicate_encode('Yarrr'))