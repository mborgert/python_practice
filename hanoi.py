# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:39:20 2020

@author: borge
"""

#want to move n-1 disks to pole b using pole c 
#ex with 2, move 1 to b, 2 to c, 1 to c. can only
#ex with 3, move top 2 to b, then 3 to c, then the top 2 to c
#think with case of n = 2 
#move n to c

def tower(n, start, end, middle):
    if(n == 1):
        print(("Move %i from tower %s to tower %s") %(n, start, end))
    else:
        tower(n-1, start, middle, end)
        print(("Move %i from tower %s to tower %s") %(n, start, end))
        tower(n-1, middle, end, start)
        
tower(2, "A","C","B")
