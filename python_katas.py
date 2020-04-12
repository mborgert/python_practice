# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:02:34 2020

@author: borge
"""
#removing vowls
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiouAEIOU")

disemvowel("doot")
