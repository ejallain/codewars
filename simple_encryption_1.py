# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:15:54 2017

@author: eria
"""


def decrypt(encrypted_text, n):
    
    while n > 0:
        split, remainder = divmod(len(encrypted_text),2)
        text_a, text_b = encrypted_text[:split], encrypted_text[split:]
        decrypted_text = ''
        for i in range(split + remainder):
            decrypted_text = decrypted_text + text_b[i]
            try:
                decrypted_text = decrypted_text + text_a[i]
            except: pass
        encrypted_text = decrypted_text
        n = n - 1
    return(encrypted_text)
        


def encrypt(text, n):
    while n > 0:
        text = text[1::2] + text[::2]
        n = n - 1
    return(text)

