# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:44:05 2020

@author: borge
"""

import numpy as np

mat = np.matrix([[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1,1,1,0,0]])
mat

 
def num_islands(graph):
    graph = graph.copy()
    row = np.size(graph,0)
    col = np.size(graph,1)
    count = 0
    
    for i in range(row):
        for j in range(col):
            if graph[i,j] == 1:
                dfs(graph, row, col, i ,j) #adds 1 to island counts and then turns it to 0's 
                count += 1
    return count

def dfs(graph, row, col, x, y):
    if (x<0 or y<0 or x>row-1 or y>col-1 or graph[x,y] == 0): #exit thing for recursion
        return
    graph[x,y] = 0 #turns the 1's to 0's 
    
    dfs(graph,row,col,x-1,y) #recursion around the matrix point, first are up, down, left, right
    dfs(graph,row,col,x+1,y)    
    dfs(graph,row,col,x,y-1)
    dfs(graph,row,col,x,y+1)
    dfs(graph,row,col,x+1,y-1) #diagonals
    dfs(graph,row,col,x+1,y+1)
    dfs(graph,row,col,x-1,y-1)
    dfs(graph,row,col,x-1,y+1)
    
        
num_islands(mat)

mat
